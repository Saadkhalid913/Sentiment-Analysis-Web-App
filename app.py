from flask import Flask, request, send_file
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin
from Model import MakePred




app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('text_added', namespace='/')
def Eval(text: str):
    results = MakePred(text)
    print(results, "\n\n")
    socketio.emit('sentiments_changed', results, namespace='/')



@app.route("/", methods = ["GET"])
@cross_origin()
def main():
    return {"hello": "This is the first object!"}



if __name__ == "__main__":
    socketio.run(app, debug=False)