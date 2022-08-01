from flask import jsonify

heroes = [{'name': 'billy connolly', 'nationality': 'scottish', 'occupation': 'comedian'},
          {'name': 'elon musk', 'nationality': 'south african', 'occupation': 'entrepreneur'},
          {'name': 'iron man', 'nationality': 'usa', 'occupation': 'billionaire'}
          ]


def index():
    return "Hello World"


def db():
    return "Hello DB Grads"


def user_profile(id):
    return f"profile page of user #{id}"


def hero():
    return jsonify(heroes)
