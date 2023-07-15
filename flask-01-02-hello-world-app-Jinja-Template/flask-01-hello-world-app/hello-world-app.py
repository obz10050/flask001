from flask import Flask



app = Flask(__name__)

@app.route("/home")
def home():
    return "hello from flask!"

# @app.route("/profile/<string:user>")
# def profile(user):
#     return "hello" + user

if __name__== "__main__":
     app.run(host="0.0.0.0", port=4000)