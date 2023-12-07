from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return ({
        "status": "success",
        "message": "api running",
        "data": []
    }, 200)


if __name__ == "__main__":
    app.run()