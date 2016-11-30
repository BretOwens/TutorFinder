from flask import Flask
from flask import render_template
from flask import request
import pymysql

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://m462isa2dh6cvxue:jfl50lzw43d657yq@nt71li6axbkq1q6a.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/rumyr9ysvijlvzqd?sslca=rds-combined-ca-bundle.pem&ssl-verify-server-cert'
#db = SQLAlchemy(app)

# Connect to the database
connection = pymysql.connect(host='nt71li6axbkq1q6a.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                             user='m462isa2dh6cvxue',
                             password='jfl50lzw43d657yq',
                             db='rumyr9ysvijlvzqd',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def hello_world():
    #return 'Hello World! - Michael'
	return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)
