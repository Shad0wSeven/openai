from flask import Flask,send_file,send_from_directory
from flask import request, redirect, url_for,jsonify
import subprocess
from werkzeug.utils import secure_filename
import os 
import urllib.request
import ssl

# make it unsafe
ssl._create_default_https_context = ssl._create_unverified_context




app = Flask(__name__)

app.config['CLIENT_RESULT'] = "./result.mp4"

@app.route("/check")
def check():
	return "OK"

@app.route("/")
def base():
	try:
		url = request.args.get('url')
		text = request.args.get('text')
		with open('input.txt', 'w') as f:
			f.write(text)
		# input written

		# find video
		try:
			urllib.request.urlretrieve(url, 'input.mp4') 

		except:
			return "Failed, no active url!"


		subprocess.call(['sh', './run.sh'])
		return send_from_directory(directory=app.root_path, path="./result.mp4", as_attachment=True)

		# now take input video and run python file on it
	except TypeError:
		return "provide url and text!!!!"
	


@app.route('/get',methods = ['GET','POST'])
def get_csv():
    try:
        return send_from_directory(directory=app.root_path, path="./result.mp4", as_attachment=True)
    except FileNotFoundError:
        abort(404)


ALLOWED_EXTENSIONS = set(['mp4'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save("./input.mp4")
		resp = jsonify({'message' : 'File successfully uploaded'})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are mp4'})
		resp.status_code = 400
		return resp
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)