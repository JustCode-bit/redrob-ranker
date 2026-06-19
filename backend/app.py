from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Redrob AI Ranker Running"
    }

if __name__ == "__main__":
    app.run(debug=True)