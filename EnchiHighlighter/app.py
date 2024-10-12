from flask import Flask, jsonify

app = Flask(__name__)

Keywords = {
    #operators array within a dictionary
    "operators": ["+", "-", "*", "/", "="]


}