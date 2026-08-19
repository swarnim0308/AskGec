import os
import string
import random
from flask import Flask, request, render_template, send_file, session, jsonify, send_from_directory
from infer import *

app = Flask(__name__, template_folder='static', static_folder='static')

# Enable ngrok optionally if specified in environment, otherwise default to local server
if os.environ.get("USE_NGROK") == "1":
    try:
        from flask_ngrok import run_with_ngrok
        run_with_ngrok(app)
    except Exception as e:
        print(f"Could not initialize ngrok: {e}")

@app.route('/', methods=['GET', 'POST'])
def home(bot_id = 'Government Engineering College Bilaspur'):
	if bot_id not in table:
		create_bot()
	if request.method == 'POST':
		if bot_id in table:
			context = table[bot_id]['context']
			question = request.form.get('ques');
			prev_q = request.form.get('prev_q');
			prev_a = request.form.get('prev_a');
			answer = iq.predict(context, question, prev_q, prev_a)			
			return answer
	if request.method == 'GET':
		if bot_id not in table:
			bot_id = "Oops! Bot not found!"
			bot_im = ""
		else:
			bot_im = table[bot_id]["im_url"]
		return render_template('index.html', bot=bot_id, bot_im=bot_im)

def create_bot():
	file = open("knowledgebase.txt", "r")
	bot_id = "Government Engineering College Bilaspur"
	context = file.read()
	file.close()
	bot_im = "https://cdn.mee6.xyz/assets/logo.png"
	table[bot_id] = {"context": context, "bot_name": bot_id, "im_url": bot_im}

table = {}
iq = InferCoQA('model')

if __name__ == '__main__':
    print("Starting AskGec local server on http://127.0.0.1:5000 ...")
    app.run(host='127.0.0.1', port=5000, debug=False)

