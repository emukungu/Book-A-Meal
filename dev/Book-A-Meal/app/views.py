from flask import (
    jsonify, request, redirect,
    url_for, render_template
)
from app import app, user_list
from .models import User

# these are controller functions

@app.route("/auth/signup", methods= ['POST'])
def signup():
    #return jsonify({'message' : 'it works'})
    #authentication
    if request.method == 'POST':
        data = request.json  # get the post data from request 
        # initalise response
        response = {
            "status": "fail",
            "message": "user not created"
        }
        # extract data from request and store it in local vars
        username = data.get('username', None)
        password = data.get('password', None)

        if username != None and password != None or username != "" and password != "":  # always ensure username and password are provided
            user_list.append(User(username=username, password=password))  # create an instance of user and add it to user_list
            response['message'] = "user created"
            response['status'] = "ok"
            print(user_list)

        return jsonify(response)


@app.route("/auth/login", methods= ['POST'])
def login():
    data = request.json  # get the post data from request 
    # initalise response
    response = {
        "status": "fail",
        "message": "user failed to login"
    }
    # extract data from request and store it in local vars
    username = data.get('username', None)
    password = data.get('password', None)

    if username != None and password != None or username != "" and password != "":
        for user in user_list:
            if user._username == username and user._password == password:
                # hooray! we have user
                response['message'] = "user logged in sucessfully"
                response['status'] = "ok"
                break
            
        return jsonify(response)