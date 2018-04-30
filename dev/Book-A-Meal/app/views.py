from flask import jsonify, request
from app import app, user_list, meal_list
from .models import User, Meals

@app.route("/auth/signup", methods=['POST'])
def signup():
    response = {
        'message':''
    }
    data = request.get_json()
    firstName = data['firstName']
    lastName = data['lastName']
    password = data['password']
    
    if firstName == '' and lastName == '' and password == '':
        response = {
            'message': "yeeee"
        }
    else:
        user = User(firstName=firstName, lastName=lastName, password=password)
        user_list.append(user)
        response['message'] = 201

    return jsonify(response)
            
            
