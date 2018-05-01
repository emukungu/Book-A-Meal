from flask import jsonify, request, json
from app import app, user_list, meal_list, menu_list, orders_list
from .models import User, User_logged_in, Meals, Menu, Orders

@app.route("/auth/signup", methods=['POST'])
def signup():
    response = {
        'message':''
    }
    data = request.json
    
    firstName = data['firstName'] 
    lastName = data['lastName']
    password = data['password']
    
    if firstName == '' and lastName == '' and password == '':
        response = {
            'message': 'Empty'
        }
        return jsonify(response),400
    else:
        user = User(firstName=firstName, lastName=lastName, password=password)
        user_list.append(user)
        response['message'] = 'User created'

        return jsonify(response),201
            
            
@app.route("/auth/login", methods = ['POST'])
def login():
    response = {
        'message':''
    }
    data = request.json
    username = data['username']
    password = data['password']

    if username == '' and password == '' or username == None and password == None:
        response = {
            'message': 'Empty'
        }
        return jsonify(response),401
    else:
        user = User_logged_in(username=username, password=password)
        user_list.append(user)
        response['message'] = 'User logged in'

        return jsonify(response),200


