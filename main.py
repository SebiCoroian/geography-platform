from flask import Flask
app = Flask(__name__)

@app.route("/test")
def hello():
    print("works")
    return
# print("nyez")
