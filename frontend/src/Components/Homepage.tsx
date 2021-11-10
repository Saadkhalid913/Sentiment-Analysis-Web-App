import React, { Component } from 'react'
import TextEditor from './TextEditor'

interface HomepageProps {
    setText: (text: string) => void
}
export default class Homepage extends Component<HomepageProps> {
    state = {}

    render() {
        return (
            <div className = "homepage">
                <TextEditor onTextChange = {s => this.props.setText(s)}/>
            </div>
        )
    }
}

