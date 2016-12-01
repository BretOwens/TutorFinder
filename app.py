from flask import Flask
from flask import render_template
from flask import request
import pymysql

app = Flask(__name__)

def execsql(query):
	connection = pymysql.connect(host='nt71li6axbkq1q6a.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
             user='m462isa2dh6cvxue',
             password='jfl50lzw43d657yq',
             db='rumyr9ysvijlvzqd',
             charset='utf8mb4',
             cursorclass=pymysql.cursors.DictCursor,
			 autocommit=True)

	cursor = connection.cursor()
	cursor.execute(query)
	results = cursor.fetchall()
	connection.close()
	cursor.close()
	return results

def insertSignup(accType, email, password, name):
	print email, password, name, accType
	print type(email), type(password), type(name), type(accType)
	connection = pymysql.connect(host='nt71li6axbkq1q6a.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
             user='m462isa2dh6cvxue',
             password='jfl50lzw43d657yq',
             db='rumyr9ysvijlvzqd',
             charset='utf8mb4',
             cursorclass=pymysql.cursors.DictCursor,
			 autocommit=True)
	cursor = connection.cursor()
	if (accType == "Tutor"):
		cursor.execute("INSERT INTO Tutor VALUES ('" + email + "', '" + password + "', '" + name + "', " + str(0) + ")")
	elif (accType == "Student"):
		cursor.execute("INSERT INTO Student VALUES ('" + email + "', '" + password + "', '" + name + "')")
	connection.commit()
	connection.close()
	cursor.close()
	return


@app.route('/')
def home_page():
	return render_template('index.html')

@app.route('/submit/')
def submit_page():
	results = execsql("SELECT CourseCode FROM Course")
	return render_template('submit.html', results=results)

@app.route('/submit/submit_post', methods=['POST'])
def submit_form():
	data = request.form
	return render_template('success.html')

@app.route('/signup/')
def signup_page():
	return render_template('signup.html')

@app.route('/signup/signup_post', methods=['POST'])
def signup_form():
	data = request.form
	insertSignup(str(data['type']), str(data["email"]), str(data["password"]), str(data["name"]))
	return render_template('success.html')

@app.route('/students/')
def students_page():
	return render_template('students.html') 

@app.route('/tutors/')
def tutors_page():
	return render_template('tutors.html')

if __name__ == '__main__':
    app.run(debug=True)
