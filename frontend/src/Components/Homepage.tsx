import React, { Component } from 'react'
import TextEditor from './TextEditor'
export default class Homepage extends Component {
    state = {}

    render() {
        return (
            <div className = "homepage">
                <TextEditor onTextChange = {s => console.log(s)}/>
            </div>
        )
    }
}

