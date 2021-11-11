import React, { Component } from 'react';
import TextEditor from './TextEditor';
import Sentiments from "./Sentiments";
import { Sentiment } from './@types';
interface HomepageProps {
    setText: (text: string) => void;
    Sentiments: Sentiment[] | undefined 
}
export default class Homepage extends Component<HomepageProps> {
    state = {}

    render() {
        return (
            <div className = "homepage">
                <TextEditor onTextChange = {s => this.props.setText(s)}/>
                <Sentiments Sentiments = {this.props.Sentiments} />
            </div>
        )
    }
}

