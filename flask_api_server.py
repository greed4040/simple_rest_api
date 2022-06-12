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
def my_endpoint_function():
    return {"status":str(datetime.datetime.now()),"resp":"serega_molodec_no_params"}

@app.route('/my_post_endpoint', methods=['POST'])
def my_endpoint_post_function():
    return {"status":str(datetime.datetime.now()),"resp":"post_request_no_params"}

@app.route('/get_data', methods=['GET'])
def get_data_function():
    #print("!"*20)
    input_args = request.args
    print(input_args)

    answer_dic = {"resp":"empty"}
    if "name" in input_args:
        if input_args["name"]=="holly" and input_args["id"]=="2": 
            print("the name is correct")
            answer_dic["resp"]="correct"
            answer_dic["date_time"]=str(datetime.datetime.now())
        if input_args["name"]=="jane": 
            answer_dic["resp"]="hello jane"
    
    return answer_dic

@app.route('/post_data', methods=['POST'])
def post_data_function():
    input_dictionary=request.json
    print(input_dictionary, type(input_dictionary))
    answer_dic = {"resp":"empty"}
    if "name" in input_dictionary:
        if input_dictionary["name"]=="bob" and input_dictionary["id"]==155: 
            answer_dic["resp"]="correct"
            answer_dic["date_time"]=str(datetime.datetime.now())
        if input_dictionary["name"]=="samantha": 
            answer_dic["resp"]="hello samantha"
 
    return answer_dic

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9020, ssl_context=('./keys/fullchain.pem', './keys/privkey.pem'))
