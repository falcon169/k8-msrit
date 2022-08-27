from flask import Flask
import socket
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python!"+socket.gethostbyname(socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0')
