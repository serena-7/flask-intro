"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
    <head>
      <title>Home</title>
    </head>
      <h1>Hi! This is the home page.</h1>
      <a href="/hello">CLICK HERE</a>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
    <h1>Hi There!</h1>
    <form action="/greet">
      What's your name? <input type="text" name="person"> <br>
      Choose a greeting: <br>
      <input type="radio" id="awesome" name="compliment" value="awesome"> awesome <br>
      <input type="radio" id="terrific" name="compliment" value="terrific"> terrific <br>
      <input type="radio" id="fantastic" name="compliment" value="fantastic"> fantastic <br>
      <input type="radio" id="neato" name="compliment" value="neato"> neato <br>
      <input type="radio" id="fantabulous" name="compliment" value="fantabulous"> fantabulous <br>
      <input type="radio" id="wowza" name="compliment" value="wowza"> wowza <br>
      <input type="radio" id="brilliant" name="compliment" value="brilliant"> brilliant <br>
      <input type="submit" value="Submit">
    </form>
  </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")
    
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
