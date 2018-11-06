import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
	return (
		"This app is working!<br/>"
		"Get the servce: <a href='/getkey'>Get Key</a>"
	)

@app.route("/getkey")
def getkey():
	data = {
		'user': 'some-user',
		'key' : 'Te98w@iim$#'
	}
	return json.dumps(data)

if __name__ == "__main__":
	app.run()
