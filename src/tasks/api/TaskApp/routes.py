from . import app
from flask import render_template
import src.tasks.database.tasks_db as tdb

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/tasks/<int:user_id>', methods=['GET'])
def view_tasks(user_id: int = 1):
	tasks = tdb.get_tasks_from_db(user_id)
	return render_template('tasks.html', tasks=tasks, user_id=user_id)


@app.route('/tasks/add', methods=['POST'])
def add_new_task():
	pass


@app.route('/tasks/daily-tasks/<string:day>', methods=['GET'])
def view_daily_tasks(day:str):
	pass


@app.route('/tasks/university-tasks', methods=['GET'])
def view_university_tasks():
	pass


@app.route('/tasks/home-tasks', methods=['GET'])
def view_home_tasks():
	pass
