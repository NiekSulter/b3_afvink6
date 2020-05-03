from flask import Flask, render_template, request, url_for, redirect
from db import load_messages, insert_message

app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def display():
    if request.method == 'POST':
        username = request.form['gebr']
        password = request.form['wachtw']
        zoekterm = request.form['zoek']
        messages, dates, time, user = load_messages(username, password, zoekterm)

        return render_template('index.html', user=user, messages=messages, dates=dates, time=time)
    else:
        return render_template('index.html')

@app.route('/plaats', methods=['GET', 'POST'])
def piep_plaatsen():
    if request.method == 'POST':
        u = request.form['plaats-u']
        p = request.form['plaats-w']
        b = request.form['plaats-b']
        insert_message(u,p,b)
        return redirect(url_for('hello_world'))
    return render_template('plaats.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
