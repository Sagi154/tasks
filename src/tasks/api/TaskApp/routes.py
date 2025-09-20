from datetime import datetime

from . import app
from flask import render_template, request, url_for, redirect
import src.tasks.database.tasks_db as tdb
import src.tasks.services.tasks_managment as tmg
from dataclasses import dataclass, field


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		return ""


@app.route('/tasks/<int:user_id>', methods=['GET', 'POST'])
def view_tasks(user_id: int = 1):
	tasks = tdb.get_tasks_from_db(user_id)
	return render_template('tasks.html', tasks=tasks, user_id=user_id)


@app.route('/tasks/add', methods=['GET', 'POST'])
def add_new_task():
	if request.method == 'GET':
		return render_template('add_task.html')
	elif request.method == 'POST':
		session = tmg.Tasks(user_id=1)
		course_name = request.form.get('course_name')
		day = request.form.get('day')
		description = request.form.get('description')
		deadline = request.form.get('deadline') == 'on'
		deadline_date = field(default_factory=datetime.now)
		if deadline:
			deadline_date = request.form.get('deadline_date')
		status = False
		session.add_task(description=description, course_name=course_name, day=day,deadline_date=deadline_date, deadline=deadline)
		return redirect(url_for('view_tasks', user_id=1))


@app.route('/tasks/daily-tasks/<string:day>', methods=['GET'])
def view_daily_tasks(day: str):
	pass


@app.route('/tasks/university-tasks', methods=['GET'])
def view_university_tasks():
	pass


@app.route('/tasks/home-tasks', methods=['GET'])
def view_home_tasks():
	pass
