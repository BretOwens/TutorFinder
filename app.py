from flask import Flask
from flask import render_template
from flask import request
import pymysql

app = Flask(__name__)

# Connect to the database
connection = pymysql.connect(host='nt71li6axbkq1q6a.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                             user='m462isa2dh6cvxue',
                             password='jfl50lzw43d657yq',
                             db='rumyr9ysvijlvzqd',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
sql = "SELECT * FROM Tutor"
cursor.execute(sql)
result = cursor.fetchone()
connection.close()

@app.route('/')
def hello_world():
	return render_template('index.html', username=result["TutorUsername"])

if __name__ == '__main__':
    app.run(debug=True)
