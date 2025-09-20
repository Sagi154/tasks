from src.tasks.api.TaskApp import app

if __name__ == '__main__':
	app.run(host='localhost', debug=True, port=8080)