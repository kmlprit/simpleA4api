from flask import Flask  # import class Flask from flask package.import

from routes import initialise_routes

app = Flask(__name__)  # Create a Flask object with name of Module

# The route() decorator is used to tell the Flask object which
# URL endpoint should trigger our function

# @app.route('/')

app = Flask('__name__')
initialise_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
