from flask import Flask
from random import *
app = Flask(__name__)
@app.route("/")
def home():
    random_number = randint(1, 100)
    text = f"Your random number is: {random_number}"
    return text
if __name__ == "__main__":
    app.run()
