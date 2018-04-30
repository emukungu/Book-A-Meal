import unittest 
from app import app, views
import json



class Api(unittest.TestCase):
    def setUp(self):
        self.test = app.test_client()

           
    def test_signup_empty_fields(self):
       
        res = self.test.post("/auth/signup", data = {'firstName': "", 'password':"", 'lastName':''}, content_type = 'application/json')
        self.assertEqual(res.data, 400)

    def test_signup_filled_fields(self):
        result = self.test.post("/auth/signup", data = {'firstName': 'Esther', 'password': 'mukungu', 'lastName':'Namusisi'}, content_type ='application/json')
        self.assertEqual(result.data, 201)

    def test_login_wrong_users(self):
        result = self.test.post("/auth/login", data = {'username':"", 'password':''}, content_type = 'application/json')
        self.assertEqual(result.status_code, 400)

    
    
if __name__ == "__main__":
    unittest.main()
        
        
        