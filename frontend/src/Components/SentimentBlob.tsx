import React from 'react'//@ts-ignore
import { Progress } from 'react-sweet-progress';
import "react-sweet-progress/lib/style.css";


const SentimentColours = {
    "anger": "",
    "fear": "",
    "joy": "",
    "love": "",
    "sadness": "",
    "surpirse": "",
}

const SentimentBlob = (props: {sentiment: { name: string, percentage: number }}) => {
    const percent = Math.floor((props.sentiment.percentage * 100))
    return (
        <div className = "sentiment-blob">
            <h3>{props.sentiment.name}</h3>
            <Progress color = {"#000000"} percent = {percent} symbol = {percent}/>
        </div>
    )
}

export default SentimentBlob