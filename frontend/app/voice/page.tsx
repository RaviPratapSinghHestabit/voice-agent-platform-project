"use client"

import { useState } from "react"
import { supabase } from "../../lib/supabase"

export default function VoicePage(){

const [transcript,setTranscript] = useState("")
const [response,setResponse] = useState("")
const [listening,setListening] = useState(false)

const startListening = () => {

console.log("Initializing speech recognition")

const SpeechRecognition =
(window as any).SpeechRecognition ||
(window as any).webkitSpeechRecognition

if(!SpeechRecognition){
alert("Speech Recognition not supported in this browser")
return
}

const recognition = new SpeechRecognition()

recognition.lang = "en-US"
recognition.continuous = false
recognition.interimResults = false
recognition.maxAlternatives = 1

recognition.onstart = () => {

console.log("Microphone started")
setListening(true)

}

recognition.onspeechstart = () => {

console.log("Speech detected")

}

recognition.onresult = async (event:any) => {

console.log("Speech result event fired")

const text = event.results[0][0].transcript

console.log("Recognized speech:", text)

setTranscript(text)

await sendMessage(text)

}

recognition.onerror = (event:any) => {

console.log("Speech recognition error:", event.error)

if(event.error === "no-speech"){
console.log("No speech detected, restarting microphone...")
setTimeout(()=> recognition.start(),1000)
}

}

recognition.onend = () => {

console.log("Speech recognition ended")

setListening(false)

}

recognition.start()

console.log("Speak now...")

}

const sendMessage = async(text:string)=>{

console.log("Sending text to backend:", text)

try{

const { data } = await supabase.auth.getSession()

console.log("Supabase session:", data)

const token = data.session?.access_token

const res = await fetch("http://127.0.0.1:8000/test-voice",{
method:"POST",
headers:{
"Content-Type":"application/json",
"Authorization":`Bearer ${token}`
},
body: JSON.stringify({
input_text: text,
agent_id: "default"
})
})

console.log("Backend response status:", res.status)

const result = await res.json()

console.log("Backend result:", result)

setResponse(result.response)

speak(result.response)

}catch(err){

console.log("Request failed:", err)

}

}

const speak = (text:string)=>{

console.log("Speaking response:", text)

const speech = new SpeechSynthesisUtterance(text)

speech.lang = "en-US"

window.speechSynthesis.speak(speech)

}

return(

<div className="flex flex-col items-center justify-center h-screen bg-gray-100 border p-10">

<h1 className="text-3xl mb-6 text-gray-800">
Voice Agent
</h1>

<button
onClick={startListening}
className="bg-green-500 text-white px-6 py-3 rounded"
>

{listening ? "Listening..." : "Start Talking"}

</button>

{transcript && (

<div className="mt-6 text-gray-800">
<b>You said:</b> {transcript}
</div>

)}

{response && (

<div className="mt-4 text-gray-800">
<b>AI:</b> {response}
</div>

)}

</div>

)

}