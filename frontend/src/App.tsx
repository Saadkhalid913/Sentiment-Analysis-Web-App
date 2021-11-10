import React, {useState, useEffect} from 'react';
import {io , Socket} from "socket.io-client"
import Homepage from './Components/Homepage';


function App() {
  const [socket, setSocket] = useState<Socket | undefined>();

  // useEffect(() => {
  //   const s = io("http://localhost:5000")
  //   setSocket(s)
  //   return () => {
  //     s.disconnect()
  //     return undefined
  //   }
  // }, [setSocket])


  const SendText = (text: string) => {
    if (socket) {
      socket.emit("text_added", text)
    }
  }
  return (
    <div className = "main-content-wrapper">
      <Homepage />
    </div>
  )
}

export default App;
