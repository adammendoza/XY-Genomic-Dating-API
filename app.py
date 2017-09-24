from flask import Flask
app = Flask(__name__)

@app.route('/callback')
def callback():
	return 'Great, your Awakens account has been authorized for use in XY!'