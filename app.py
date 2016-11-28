from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    #return 'Hello World! - Michael'
	return render_template('layout.html')

if __name__ == '__main__':
	app.debug = True
    app.run()
