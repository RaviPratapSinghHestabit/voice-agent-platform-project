"use client"

import { useEffect,useState } from "react"
import { useRouter } from "next/navigation"
import { createClient } from "@supabase/supabase-js"

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
)

export default function DashboardPage(){

  const router = useRouter()
  const [email,setEmail] = useState("")

  useEffect(()=>{

    const checkUser = async () => {

      const { data } = await supabase.auth.getUser()

      if(!data.user){
        router.push("/login")
        return
      }

      setEmail(data.user.email || "")
    }

    checkUser()

  },[])

  const handleLogout = async () => {

    await supabase.auth.signOut()

    router.push("/login")
  }

  return(

    <div className="min-h-screen bg-gray-100 p-10">

      <div className="max-w-4xl mx-auto bg-white p-8 rounded-xl shadow">

        <div className="flex justify-between items-center mb-6">

          <h1 className="text-2xl font-bold text-gray-800">
            Dashboard
          </h1>

          <button
          onClick={handleLogout}
          className="bg-red-500 text-white px-4 py-2 rounded-lg text-gray-800"
          >
            Logout
          </button>

          <button
          onClick={()=>router.push("/voice")}
          style={{
          marginTop:"20px",
          padding:"10px 20px",
          background:"#22c55e",
          border:"none",
          color:"white"
        }}>
        Start Voice Agent
        </button>

        </div>

        <p className="text-gray-700">
          Logged in as:
        </p>

        <p className="font-semibold mt-2 text-gray-800">
          {email}
        </p>

      </div>

    </div>
  )
}