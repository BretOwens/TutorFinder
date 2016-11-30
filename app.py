from flask import Flask
from flask import render_template
from flask import request
#from flask_sqlalchemy import SQLAlchemy
import pypyodbc

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://m462isa2dh6cvxue:jfl50lzw43d657yq@nt71li6axbkq1q6a.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/rumyr9ysvijlvzqd?sslca=rds-combined-ca-bundle.pem&ssl-verify-server-cert'
#db = SQLAlchemy(app)

myConnection = pypyodbc.connect(os.environ['DATABASE_URL'])
myCursor = myConnection.cursor()
myCursor.executre('SELECT * FROM Tutors')
rows = myCursor.fetchall();

for r in rows:
	print(f)

@app.route('/')
def hello_world():
    #return 'Hello World! - Michael'
	return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)
