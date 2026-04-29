from flask import Flask
import random
app = Flask(__name__)
@app.route("/")
def home():
    random_number = rannum(1, 100)
    text = f"Your random number is: {random_number}"
    return text
if __name__ == "__main__":
    app.run()
