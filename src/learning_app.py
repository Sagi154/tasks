from flask import Flask, request, make_response,render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
	my_Value = "Hello from Flask!"
	my_result = 3 + 5
	mylist = ["Apple", "Banana", "Cherry"]
	return render_template('index.html', mylist=mylist)

@app.route('/other')
def other():
	some_text = "This is some other text. with lllllots of l's"
	return render_template('other.html', some_text=some_text)

@app.route('/redirect_endpoint')
def redirect_endpoint():
	return redirect(url_for('other'))

@app.template_filter('reverese')
def reverse_filter(s):
	return s[::-1]

@app.route('/hello')
def hello():
	response = make_response('Hello World\n')
	response.status_code = 202
	response.headers['content-type'] = 'text/plain'
	return response


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


@app.route('/hello', methods=['POST', 'GET'])
def hello_post_get():
	if request.method == 'POST':
		return "<h1>Hello via POST!</h1>"
	else:
		return "<h1>Hello via GET!</h1>"

if __name__ == '__main__':
	app.run(host='localhost', debug=True, port=8080)