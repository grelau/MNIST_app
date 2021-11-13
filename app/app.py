from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():

    return "Demo Flask & Docker application is up and running!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)