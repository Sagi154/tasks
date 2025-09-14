from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
	return "<h1>Hello, World!</h1>"


@app.route('/hello')
def hello():
	return "<h1>Hello from the /hello route!</h1>"


@app.route('/greet/<name>')
def greet(name):
	return f"<h1>Hello, {name}!</h1>"


@app.route('/quickmafs/<int:a>/<int:b>')
def quickmafs(a, b):
	return f"<h1>{a} + {b} = {a + b}</h1>"


@app.route('/handle_url_params')
def handle_url_parms():
	if 'greeting' in request.args.keys() and 'name' in request.args.keys():
		greeting = request.args['greeting']
		name = request.args.get('name')
		return f'{greeting}, {name}'
	else:
		return "Error: Please provide both a greeting and a name in the URL parameters."

	# return str(request.args)
	# return "<h1>This route can handle URL parameters!</h1>"


if __name__ == '__main__':
	app.run(host='localhost', debug=True, port=8080)