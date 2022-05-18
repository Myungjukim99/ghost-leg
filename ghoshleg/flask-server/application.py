from flask import Flask
from flask import Flask,render_template




app = Flask(__name__)
app.config["SECRET_KEY"]="ABCD"

@app.route('/')
def hello_world():
    return  render_template('ladder.html')


if __name__ == '__main__':
    app.run()


