from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("hellow world")
    return "Flask app running on Azure 🚀"

if __name__ == "__main__":
    app.run()