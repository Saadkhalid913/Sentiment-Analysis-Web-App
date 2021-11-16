import React from 'react'
import RichEditorExample from './RichTextEditor'


interface TextEditorProps {
    onTextChange: (text: string) => void;
}

const TextEditor = (props: TextEditorProps) : JSX.Element => {
    return <RichEditorExample onChange = {(s:any) => {
        if (s[s.length - 1] === " ")
            props.onTextChange(s)
    }}  />
} 

export default TextEditor
