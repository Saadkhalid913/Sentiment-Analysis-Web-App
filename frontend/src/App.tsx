import React, {useState, useEffect} from 'react';
import {io , Socket} from "socket.io-client"
import Homepage from './Components/Homepage';


function App() {
  const [socket, setSocket] = useState<Socket | undefined>();

  // @ts-ignore
  useEffect(() => {
    console.log("rendering")
    const s = io("http://localhost:5000")
    setSocket(s)
    return () => s.disconnect()

  }, [setSocket])


  const SendText = (text: string) => {
    if (socket) {
      console.log("Sending current text")
      socket.emit("text_added", text)
    }
  }  


  return (
    <div className = "main-content-wrapper">
      <Homepage setText = {SendText}/>
    </div>
  )
}

export default App;
