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
def home_page():
	return render_template('index.html', username=result["TutorUsername"])

@app.route('/submit/')
def submit_page():
	return render_template('submit.html', username=result["TutorUsername"])

@app.route('/signup/')
def signup_page():
	return render_template('signup.html', username=result["TutorUsername"])

@app.route('/students/')
def students_page():
	return render_template('students.html', username=result["TutorUsername"])

@app.route('/tutors/')
def tutors_page():
	return render_template('tutors.html', username=result["TutorUsername"])

@app.route('/signup/form_post', methods=['POST'])
def complete_form():
	data = request.form['data']
	return render_template('success.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
