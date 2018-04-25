from flask import Flask

app = Flask(__name__)

# This will hold all users created on signup
user_list = []

from app import views