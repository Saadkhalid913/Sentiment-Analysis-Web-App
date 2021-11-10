from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin




app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["GET"])
@cross_origin()
def main():
    return {"hello": "This is the first object!"}



if __name__ == "__main__":
    app.run()