import flask

app = flask.Flask(__name__)

@app.route('/api/some_endpoint')
def index():
    return flask.jsonify({'data': 'some data'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
