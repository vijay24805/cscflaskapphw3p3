from flask import Flask
app = Flask('coreapp')


import views

@app.route("/")
def index():
	return 'hello'


