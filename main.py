from flask import Flask
app = Flask('yas')

# @app.route("/test")
# def hello():
#     print("works")
#     return "working"
@app.route("/")
def hello():
    print("index")
    return "index. go to /test"
# print("nyez")
