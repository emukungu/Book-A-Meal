from flask import Flask

app = Flask(__name__)

# This will hold all users created on signup
user_list = []
meal_list = []
menu_list = []
orders_list = []
list_meals = []
restaurant_list = []
from . import views

