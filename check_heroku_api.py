"""
Heroku Api test script
"""
import requests


data = {
    "age": 32,
    "workclass": "Private",
    "education": "Some-college",
    "maritalStatus": "Married-civ-spouse",
    "occupation": "Exec-managerial",
    "relationship": "Husband",
    "race": "Black",
    "sex": "Male",
    "hoursPerWeek": 60,
    "nativeCountry": "United-States"
    }
<<<<<<< HEAD
r = requests.post('https://project3-nd.herokuapp.com/', json=data)
||||||| 3c1040e
r = requests.post('https://ml-heroku-fastapi.herokuapp.com/', json=data)
=======
r = requests.post('https://test-project3.herokuapp.com/', json=data)
>>>>>>> 3a86b1ae526dd9430f116f578257c228b040cc21

assert r.status_code == 200

print("Response code: %s" % r.status_code)
print("Response body: %s" % r.json())
