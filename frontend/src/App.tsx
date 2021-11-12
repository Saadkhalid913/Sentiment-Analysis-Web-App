import React, {useState, useEffect} from 'react';
import {io , Socket} from "socket.io-client"
import { Sentiment } from './Components/@types';
import Homepage from './Components/Homepage';


const URI = process.env.NODE_ENV === "production" ? "/" : "http://localhost:5000"

function App() {
  const [socket, setSocket] = useState<Socket | undefined>();
  const [sentiments, setSentiments] = useState<Sentiment[]>();
  const DefaultSentiments = [{'name': 'anger', 'percentage': 0},
                             {'name': 'fear', 'percentage': 0},
                             {'name': 'joy', 'percentage': 0}, 
                             {'name': 'love', 'percentage': 0}, 
                             {'name': 'sadness', 'percentage': 0}, 
                             {'name': 'surprise', 'percentage': 0}]

  // @ts-ignore
  useEffect(() => {
    console.log("rendering")
    const s = io(URI)
    setSocket(s)
    return () => s.disconnect()

  }, [setSocket])

  useEffect(() => {
    if (!socket) return
    const handler = (s: Sentiment[]) => setSentiments(s)
    socket.on("sentiments_changed", handler)

    return () => {
      socket.off("sentiments_changed", handler)
      return undefined
    }
  })


  const SendText = (text: string) => {
    if (text.length === 0) {
      setSentiments(DefaultSentiments)
      return
    }
    if (socket) { 
      text = text.replace( /  +/g, ' ' )
      socket.emit("text_added", text)
    }
  }  


  return (
      <Homepage Sentiments = {sentiments} setText = {SendText} />
  )
}

export default App;