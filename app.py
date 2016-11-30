from flask import Flask
from flask import render_template
from flask import request
import pyodbc

app = Flask(__name__)

myConnection = pyodbc.connect(os.environ['DATABASE_URL'])
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
