import React from 'react';
import { Sentiment } from './@types';
import SentimentBlob from './SentimentBlob';


interface SentimentsProps {
    Sentiments: Sentiment[] | undefined;
}

const Sentiments = (props: SentimentsProps) => {
    if (!props.Sentiments || props.Sentiments.length <1 ) return <div className = "sentiment-wrapper"></div>

    props.Sentiments.sort((a, b) => b.percentage - a.percentage)
    return (<div className = "sentiment-wrapper">
                {props.Sentiments.map(s => <SentimentBlob key = {s.name} sentiment = {s} />)}
            </div>)
}

export default Sentiments;


