import React, { useState } from "react"
import api from "../api"
import { useNavigate } from "react-router-dom"
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants"

const Login = () => {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [loading, setLoading] = useState(false)
    const navigate = useNavigate()

    const route = "api/token/";


    const handleSubmit = async (e) => {
        setLoading(true)
        e.preventDefault()

        try {
            const res = await api.post(route, { username, password })
            localStorage.setItem(ACCESS_TOKEN, res.data.access)
            localStorage.setItem(REFRESH_TOKEN, res.data.refresh)
            navigate("/")
        } catch (error) {
            alert(error)
        } finally {
            setLoading(false)
        }


    }
  return (
    <div className="bg-main h-screen w-full flex flex-row gap-80 items-center justify-center ">
      <div>
        <h1 className="text-[5rem] text-white">Connect <br/>with friends <br/><b>easily &<br/> quickly</b></h1>
      </div>
      <div className=" w-[20rem] h-[33rem] 2border-solid border-primary border p-4 pt-10">
        <form onSubmit={handleSubmit} action="" className="flex flex-col gap-10 justify-center items-center">
            <h1 className="text-3xl self-center text-6xl text-primary">Login</h1>
            <input type="text" placeholder="username" className="text-sm w-full h-[30px] rounded outline-none px-1"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />
            <input type="password" placeholder="password" className="text-sm w-full h-[30px] rounded outline-none px-1"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <button type="submit" className="w-40 text-2xl  bg-primary rounded p-1">Login</button>
        </form>
      </div>
    </div>
  )
}

export default Login
