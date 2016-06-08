"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import random
import string

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
  
   
    def index(self):
        if "random_word" not in session:
            session['random_word'] = " "
        if "attempt" not in session:
            session['attempt'] = 0

        return self.load_view('index.html', random_word=session["random_word"], attempt=session["attempt"])

    def generate(self):
        if session['random_word'] != " ":
            session['random_word'] = " "
        for i in range(25):
            session['random_word'] += random.choice(string.ascii_lowercase)
        session['attempt'] += 1

        return redirect("/")