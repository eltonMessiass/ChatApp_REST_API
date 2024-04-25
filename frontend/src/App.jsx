import React from 'react'
import Home from './pages/Home'
import Login from './pages/Login'
import Register from './pages/Register'
import NotFound from './pages/NotFound'
import ProtectedRoute from './components/ProtectedRoute'
import { BrowserRouter,Routes,Route, Navigate } from 'react-router-dom'

function App() {
  return (
      <div>
        <BrowserRouter>
          <Routes>
            <Route path='/' element={<ProtectedRoute> <Home/> </ProtectedRoute>}/>
            <Route path='/login' element={<Login/>}/>
            <Route path='/register' element={<Register/>}/>
            <Route path='*' element={<NotFound/>}/>
          </Routes>
        </BrowserRouter>
      </div>
    )
}

export default App
