from flask import Flask
from flask import json
from flask import request
from flask import jsonify
from flask_cors import CORS
import time
import datetime
#import mysql.connector
import string
import random
import hashlib

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/my_endpoint', methods=['GET'])
def my_endpoint():
    print(request)

    print(datetime.datetime.now())

    return {"status":"ok","resp":"karina_molodec"}

@app.route('/get_data', methods=['GET'])
def get_data():
    input_args = request.args
    print(request)
    print(input_args)
    print(datetime.datetime.now())

    answer_dic = {"status":"ok","resp":"default"}
    if "name" in input_args:
        if input_args["name"]=="holly": 
            print("the name is correct"); answer_dic["resp"]="correct"
        if input_args["name"]=="karina": answer_dic["resp"]="hello karina"
    
    return answer_dic

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9020, debug=True, ssl_context=('./keys/fullchain.pem', './keys/privkey.pem'))
