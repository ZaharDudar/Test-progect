from flask import Flask, render_template, request, redirect

app = Flask(__name__)

messages = []
@app.route('/messages')
def hello():
  return render_template('messages.html', name='guest', messages=messages)

@app.route('/add_message', methods=['GET'])
def show_create_msg_form():
  return render_template('add_msg.html', name='guest', messages=messages)

@app.route('/add_message', methods=['POST'])
def add_message():
  messages.append({'name': request.form['fio'], 'text': request.form['msg']})
  return redirect('/messages')