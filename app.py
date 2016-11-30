from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def hello_world():
    #return 'Hello World! - Michael'
	return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)
