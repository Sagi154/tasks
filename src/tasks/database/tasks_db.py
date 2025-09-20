from src.tasks.models.Task import Task
import psycopg2

CONN_DICT = {
	'host': 'localhost',
	'port': '5432',
	'dbname': 'task_app',
	'user': 'sagi1',
	'password': 'tdbsagi'
}
TABLE_NAME = 'Tasks'

# TODO: Add logging to database operations


def get_all_tasks_from_db() -> list[Task]:
	"""
	Get all tasks from the database.
	:return: A list of Task objects
	"""
	tasks = []
	with psycopg2.connect(**CONN_DICT) as conn:
		command = f"""SELECT * FROM {TABLE_NAME};"""
		cur = conn.cursor()
		cur.execute(command)
		conn.commit()
		rows = cur.fetchall()
		columns = [desc[0] for desc in cur.description]
	for row in rows:
		task_dict = dict(zip(columns, row))
		task = Task(**task_dict)
		if task:
			tasks.append(task)
	return tasks


def get_task_from_db(user_id: int, task_id: int) -> Task:
	"""
	Get a task from the database using the task ID.
	:param user_id: The ID of the user the task belongs to
	:param task_id: The ID of the task
	:return: A Task object or None if not found
	"""
	with psycopg2.connect(**CONN_DICT) as conn:
		command =f"""SELECT * FROM {TABLE_NAME} WHERE user_id = %s AND task_id = %s;"""
		cur = conn.cursor()
		cur.execute(command, (user_id, task_id))
		conn.commit()
		row = cur.fetchone()
		columns = [desc[0] for desc in cur.description]
	if row is None:
		return None
	task_dict = dict(zip(columns, row))
	task_dict.pop('user_id')
	task = Task(**task_dict)
	return task if task else None


def get_tasks_from_db(user_id: int) -> list[Task]:
	"""
	Get all tasks from the database for a specific user.
	:param user_id: The ID of the user the tasks belong to
	:return: A list of Task objects
	"""
	tasks = []
	with psycopg2.connect(**CONN_DICT) as conn:
		command = f"""SELECT * FROM {TABLE_NAME} WHERE user_id = %s;"""
		cur = conn.cursor()
		cur.execute(command, (user_id,))
		conn.commit()
		rows = cur.fetchall()
		columns = [desc[0] for desc in cur.description]
	for row in rows:
		task_dict = dict(zip(columns, row))
		task_dict.pop('user_id')
		task = Task(**task_dict)
		if task:
			tasks.append(task)
	return tasks

def get_tasks_from_db_by_day(user_id: int, day: str) -> list[Task]:
	"""
	Get all tasks from the database for a specific user and day.
	:param user_id: The ID of the user the tasks belong to
	:param day: The day of the week to filter tasks
	:return: A list of Task objects
	"""
	tasks = []
	with psycopg2.connect(**CONN_DICT) as conn:
		command = f"""SELECT * FROM {TABLE_NAME} WHERE user_id = %s AND day = %s;"""
		cur = conn.cursor()
		cur.execute(command, (user_id, day))
		conn.commit()
		rows = cur.fetchall()
		columns = [desc[0] for desc in cur.description]
	for row in rows:
		task_dict = dict(zip(columns, row))
		task_dict.pop('user_id')
		task = Task(**task_dict)
		if task:
			tasks.append(task)
	return tasks

def get_tasks_from_db_by_course(user_id: int, course_name: str) -> list[Task]:
	"""
	Get all tasks from the database for a specific user and course name.
	:param user_id: The ID of the user the tasks belong to
	:param course_name: The course name to filter tasks
	:return: A list of Task objects
	"""
	tasks = []
	with psycopg2.connect(**CONN_DICT) as conn:
		command = f"""SELECT * FROM {TABLE_NAME} WHERE user_id = %s AND course_name = %s;"""
		cur = conn.cursor()
		cur.execute(command, (user_id, course_name))
		conn.commit()
		rows = cur.fetchall()
		columns = [desc[0] for desc in cur.description]
	for row in rows:
		task_dict = dict(zip(columns, row))
		task_dict.pop('user_id')
		task = Task(**task_dict)
		if task:
			tasks.append(task)
	return tasks


def add_new_task_to_db(user_id: int, task: Task) -> int:
	"""
	Add a new task to the database using the Task object.
	:param user_id: The ID of the user the task belongs to
	:param task: The task to add
	:return: The task ID in the database
	"""
	with psycopg2.connect(**CONN_DICT) as conn:
		command = f"""INSERT INTO {TABLE_NAME} (user_id, course_name, day, description, deadline, deadline_date, time_created, status, time_completed) 
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING task_id;"""
		cur = conn.cursor()
		cur.execute(command, (user_id, ) + task.values())
		conn.commit()
		task_id = cur.fetchone()[0]
	return task_id


def update_task_in_db(user_id: int, task: Task) -> None:
	"""
	Update an existing task in the database using the Task object.
	:param user_id: The ID of the user the task belongs to
	:param task: The task to update
	"""
	with psycopg2.connect(**CONN_DICT) as conn:
		command = f""" UPDATE {TABLE_NAME} SET course_name = %s, day = %s, description = %s, deadline = %s, \
		 				deadline_date = %s, time_created = %s, status = %s, time_completed = %s \
						WHERE user_id = %s AND task_id = %s;"""
		cur = conn.cursor()
		cur.execute(command, task.values() + (user_id, task.task_id))
		conn.commit()


def remove_task_from_db(user_id: int, task_id: int) -> None:
	"""
	Remove the task from the database using the task ID.
	:param user_id: The ID of the user the task belongs to
	:param task_id: The ID of the task to remove
	"""
	with psycopg2.connect(**CONN_DICT) as conn:
		command = f"""DELETE FROM {TABLE_NAME} WHERE user_id = %s AND task_id = %s;"""
		cur = conn.cursor()
		cur.execute(command, (user_id, task_id))
		conn.commit()
		# if cur.rowcount == 0:
		# 	print(f"Task {task_id} not found for user {user_id}")
		# else:
		# 	print(f"Task {task_id} removed from the database")


if __name__ == "__main__":
	# Example usage
	user_id = 1
	task_id = 3
	task = get_task_from_db(user_id, task_id)
	print(task)
