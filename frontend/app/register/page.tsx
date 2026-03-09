"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { createClient } from "@supabase/supabase-js"

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
)

export default function RegisterPage() {

  const router = useRouter()

  const [email,setEmail] = useState("")
  const [password,setPassword] = useState("")
  const [error,setError] = useState("")
  const [loading,setLoading] = useState(false)

  const handleRegister = async (e:any) => {

    e.preventDefault()

    setLoading(true)
    setError("")

    const { error } = await supabase.auth.signUp({
      email,
      password
    })

    setLoading(false)

    if(error){
      setError(error.message)
      return
    }

    router.push("/login")
  }

  return(

    <div className="min-h-screen flex items-center justify-center bg-gray-100">

      <div className="bg-white p-8 rounded-xl shadow-md w-full max-w-md">

        <h2 className="text-2xl font-bold text-center mb-6 text-gray-800">
          Create Account
        </h2>

        <form onSubmit={handleRegister} className="space-y-4">

          <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e)=>setEmail(e.target.value)}
          className="w-full p-3 border rounded-lg text-gray-800"
          required
          />

          <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e)=>setPassword(e.target.value)}
          className="w-full p-3 border rounded-lg text-gray-800"
          required
          />

          {error && (
            <p className="text-red-500 text-sm">
              {error}
            </p>
          )}

          <button
          type="submit"
          className="w-full bg-black text-white p-3 rounded-lg hover:opacity-90"
          disabled={loading}
          >
            {loading ? "Creating..." : "Register"}
          </button>

        </form>

      </div>

    </div>
  )
}