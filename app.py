import flask

app = flask.Flask(__name__)

@app.route('/api/some_endpoint')
def some_endpoint():
    return flask.jsonify({'data': 'some really cool data from pr-service-1'})

@app.route('/')
def index():
    return 'hello from /'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
