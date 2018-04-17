from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def get_ip():
    return f'Your public IP address is: {request.remote_addr}'
