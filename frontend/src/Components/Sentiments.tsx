import React from 'react';
import { Sentiment } from './@types';
import SentimentBlob from './SentimentBlob';


interface SentimentsProps {
    Sentiments: Sentiment[] | undefined;
}

const Sentiments = (props: SentimentsProps) => {
    if (!props.Sentiments || props.Sentiments.length <1 ) return <div className = "sentiment-wrapper"></div>
    return (<div className = "sentiment-wrapper">
                {props.Sentiments.map(s => <SentimentBlob sentiment = {s} />)}
            </div>)
}

export default Sentiments;


