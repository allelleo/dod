import flask

app = flask.Flask(__name__)

messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        return flask.render_template('index.html', messages=messages)
    else:
        messages.append(flask.request.form['msg'])
        return flask.render_template('index.html', messages=messages)
    
app.run(debug=True)