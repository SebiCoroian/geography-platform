from flask import Flask
app = Flask('yas')

@app.route("/test")
def hello():
    print("works")
    return "working"
# print("nyez")
