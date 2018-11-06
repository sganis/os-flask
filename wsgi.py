import json
from flask import Flask

application = Flask(__name__)

@application.route("/")
def root():
	return (
		"<br/><br/><br/><br/>"
		"<center>"
		"<h1>This app is working!"
		"<br/>"
		"Test service: <a href='/getkey'>Get Key</a></h1>"
		"</center>"
	)

@application.route("/getkey")
def getkey():
	data = {
		'user': 'some-user',
		'key' : 'Te98w@iim$#'
	}
	return json.dumps(data)

if __name__ == "__main__":
	application.run()

# openshift webhook
# https://master.aramco-6a76.openshiftworkshop.com:443/apis/build.openshift.io/v1/namespaces/os-flask/buildconfigs/os-flask/webhooks/65ab01535f80037f/github