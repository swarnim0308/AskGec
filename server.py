from flask import Flask, request, render_template
from flask import send_file,session,jsonify
import string
import random
from infer import *
from flask_ngrok import run_with_ngrok



def id_generator(size=4, chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))

app = Flask(__name__,template_folder='static')

run_with_ngrok(app)

@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'),   filename)

@app.route('/',methods=['GET', 'POST'])
def home(bot_id = 'Government Engineering College Bilaspur'):
	if bot_id not in table:
		create_bot()
	if request.method == 'POST':
		if bot_id in table:
			context = table[bot_id]['context']
			question = request.form.get('ques');
			prev_q = request.form.get('prev_q');
			prev_a = request.form.get('prev_a');
			answer = iq.predict(context,question,prev_q,prev_a)			
			return answer
	if request.method == 'GET':
		if bot_id not in table:
			bot_id = "Oops! Bot not found!"
			bot_im = ""
		else:
			bot_im = table[bot_id]["im_url"]
		return render_template('index.html',bot=bot_id,bot_im=bot_im)

def create_bot():
	file = open("knowledgebase.txt","r")
	bot_id = "Government Engineering College Bilaspur"
	context = file.read()
	bot_im = "https://cdn.mee6.xyz/assets/logo.png"
	table[bot_id] = {"context":context,"bot_name":bot_id,"im_url":bot_im}


table = {}
iq = InferCoQA('model')

app.run()
