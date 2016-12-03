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

def addCourse(email, course, pay):
	connection = pymysql.connect(host='nt71li6axbkq1q6a.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
             user='m462isa2dh6cvxue',
             password='jfl50lzw43d657yq',
             db='rumyr9ysvijlvzqd',
             charset='utf8mb4',
             cursorclass=pymysql.cursors.DictCursor,
			 autocommit=True)
	cursor = connection.cursor()
	cursor.execute("INSERT INTO Can_Tutor VALUES ('" + email + "', '" + course + "', '" + pay + "')")
	connection.commit()
	connection.close()
	cursor.close()
	return

def updateAccount(accType, email, name):
	connection = pymysql.connect(host='nt71li6axbkq1q6a.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
             user='m462isa2dh6cvxue',
             password='jfl50lzw43d657yq',
             db='rumyr9ysvijlvzqd',
             charset='utf8mb4',
             cursorclass=pymysql.cursors.DictCursor,
			 autocommit=True)
	cursor = connection.cursor()
	if (accType == "Tutor"):
		cursor.execute("UPDATE Tutor SET TutorName='" + name + "' WHERE TutorUsername='" + email + "'")
	elif (accType == "Student"):
		cursor.execute("UPDATE Student SET StudentName='" + name + "' WHERE StudentUsername='" + email + "'")
	connection.commit()
	connection.close()
	cursor.close()
	return

def deleteAccount(accType, email):
	connection = pymysql.connect(host='nt71li6axbkq1q6a.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
             user='m462isa2dh6cvxue',
             password='jfl50lzw43d657yq',
             db='rumyr9ysvijlvzqd',
             charset='utf8mb4',
             cursorclass=pymysql.cursors.DictCursor,
			 autocommit=True)
	cursor = connection.cursor()
	if (accType == "Tutor"):
		cursor.execute("DELETE FROM Tutor WHERE TutorUsername='" + email + "'")
	elif (accType == "Student"):
		cursor.execute("DELETE FROM Student WHERE StudentUsername='" + email + "'")
	connection.commit()
	connection.close()
	cursor.close()
	return

def search(accType, search):
	connection = pymysql.connect(host='nt71li6axbkq1q6a.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
             user='m462isa2dh6cvxue',
             password='jfl50lzw43d657yq',
             db='rumyr9ysvijlvzqd',
             charset='utf8mb4',
             cursorclass=pymysql.cursors.DictCursor,
			 autocommit=True)
	cursor = connection.cursor()
	if (accType == "Tutor"):
		cursor.execute("SELECT TutorUsername FROM Tutor WHERE TutorUsername LIKE '" + search + "%'")
	elif (accType == "Student"):
		cursor.execute("SELECT StudentUsername FROM Student WHERE StudentUsername LIKE '" + search + "%'")
	results = cursor.fetchall()
	connection.commit()
	connection.close()
	cursor.close()
	return results

@app.route('/')
def home_page():
	return render_template('index.html')

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

@app.route('/signin/')
def signin_page():
	return render_template('signin.html')

@app.route('/signin/signin_post', methods=['POST'])
def signin_form():
	data = request.form
	accType = str(data['type'])

	courses = execsql("SELECT CourseCode FROM Course")

	results = execsql("SELECT * FROM Tutor WHERE TutorUsername='" + str(data['email']) + "'")
	name = str(results[0]['TutorName'])
	username = str(results[0]['TutorUsername'])

	return render_template('account.html', name=name, username=username, accType=accType, courses=courses)

@app.route('/signin/update_post', methods=['POST'])
def update_form():
	data = request.form
	updateAccount(str(data['type']), str(data["email"]), str(data["name"]))
	return render_template('success.html')

@app.route('/signin/delete_post', methods=['POST'])
def delete_form():
	data = request.form
	deleteAccount(str(data['type']), str(data["email"]))
	return render_template('success.html')

@app.route('/signin/add_course_post', methods=['POST'])
def add_course_form():
	data = request.form
	addCourse(str(data["email"]), str(data["course"]), str(data["pay"]))
	return render_template('success.html')

@app.route('/students/')
def students_page():
	results = execsql("SELECT * FROM Student")
	return render_template('students.html', results=results) 

@app.route('/tutors/')
def tutors_page():
	results = execsql("SELECT * FROM Tutor")
	return render_template('tutors.html', results=results)

@app.route('/tutors/<user>', methods=['GET'])
def tutors_user_page(user):
	results = execsql("SELECT * FROM Tutor WHERE TutorUsername='" + user + "'")
	name = str(results[0]['TutorName'])
	username = str(results[0]['TutorUsername'])
	return render_template('tutors_user.html', name=name, username=username)

@app.route('/courses/')
def courses_page():
	results = execsql("SELECT * FROM Course")
	return render_template('courses.html', results=results)

@app.route('/courses/<course>', methods=['GET'])
def course_code_page(course):
	results = execsql("SELECT * FROM Course WHERE CourseCode='" + course + "'")
	description = str(results[0]['CourseDescription'])
	return render_template('course_code.html', course=course, description=description)

@app.route('/search_post', methods=['POST'])
def search_form():
	data = request.form
	results = search(str(data['type']), str(data["search"]))
	return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
