from flask import Flask
from random import *
app = Flask(__name__)
@app.route("/")
def home():
    text = """
    Day 1: I made a new website. webflakes.qzz.io, it will contain this website and my projects (since i cannot get anymore domains.)
    Day 2: I made a Random Number Generator, i made it with simple HTML and a bit of CSS. I learned about Jinja and Requests because of this.
    
    
    
    """
    return text
if __name__ == "__main__":
    app.run()
