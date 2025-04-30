from datetime import datetime
from Task import Task
import pandas as pd
import tasks_db as tdb
import logging

DB_NAME = "Tasks.db"


class Tasks:
	"""
	This class represents tasks for a specific user.
	Attributes:
		user_id (int): The user's ID
		tasks (pd.DataFrame): A data frame of the user's tasks, doesn't include the user ID
	"""
	user_id: int = None
	tasks: pd.DataFrame = None

	def __init__(self, user_id: int) -> None:
		"""
		Initialize the Tasks class with the user ID and load the tasks from the database
		:param user_id: User's ID
		"""
		self.user_id = user_id
		self.tasks = tdb.get_tasks_for_user(self.user_id)
		if self.tasks is None:
			self.tasks = pd.DataFrame(columns=['task_id', 'course_name', 'day', 'description', 'deadline',
											 'deadline_date', 'time_created', 'status', 'time_completed'])

	@staticmethod
	def get_task_from_frame(task_frame: pd.DataFrame) -> Task:
		"""
		Get a task object from the data frame
		:param task_frame: The data frame representing the task
		:return: A Task object
		"""
		task = Task(
			task_id=task_frame['task_id'],
			course_name=task_frame['course_name'],
			day=task_frame['day'],
			description=task_frame['description'],
			deadline=task_frame['deadline'],
			deadline_date=task_frame['deadline_date'],
			time_created=task_frame['time_created'],
			status=task_frame['status'],
			time_completed=task_frame['time_completed']
		)
		return task

	def get_task_object(self, task_id: int) -> Task:
		"""
		Get a task object from the data frame using that task's ID
		:param task_id: The ID of the task
		:return: A task object or None if not found
		"""
		# task_frame = self.tasks.loc[(self.tasks['user_id'] == self.user_id) & (self.tasks['task_id'] == task_id)]
		task_frame = self.tasks.loc[self.tasks['task_id'] == task_id]
		if task_frame.empty:
			logging.error("Task not found")
			return None
		task = self.get_task_from_frame(task_frame.iloc[0])
		return task

	def add_task(self, description: str, course_name: str, day: str, deadline_date: datetime.date,
				 status: bool = False, deadline: bool = False ) -> None:
		"""
		Add a new task to be done
		:param description: The task description
		:param course_name: The name of the course the task is for
		:param day: The day of the week to do the task
		:param deadline_date: The task date of submission
		:param status: Is the task done or not
		:param deadline: Does the task have a deadline or not
		"""
		task = Task(description, course_name, day, deadline_date, deadline, status)
		task_id = tdb.update_task_in_db(user_id=self.user_id, task=task)
		task.update_task_id(task_id)
		new_task = pd.DataFrame([
			{
				'task_id': task.task_id,
				'course_name': task.course_name,
				'day': task.day,
				'description': task.description,
				'deadline_date': task.deadline_date,
				'deadline': task.deadline,
				'time_created': task.time_created,
				'status': task.status,
				'time_completed': task.time_completed
			}
		])
		self.tasks = pd.concat([self.tasks, new_task], ignore_index=True)

	def complete_task(self, task_id: int) -> None:
		"""
		Mark the task as completed
		:param task_id: The task ID
		"""
		# Get Task object
		task = self.get_task_object(task_id)
		if task is None:
			logging.error("Task not found")
			return
		# Update the task status
		task.mark_complete()
		#self.tasks.loc[(self.tasks['user_id'] == self.user_id) & (self.tasks['task_id'] == task_id), 'status'] = True
		self.tasks.loc[self.tasks['task_id'] == task_id, 'status'] = True
		self.tasks.loc[self.tasks['task_id'] == task_id, 'time_completed'] = task.time_completed
		tdb.update_task_in_db(user_id=self.user_id, task=task)

	def change_description(self, task_id: int, description: str) -> None:
		"""
		Change the description of a task
		:param task_id: The task ID
		:param description: The new task description
		"""
		# Get Task object
		task = self.get_task_object(task_id)
		if task is None:
			logging.error("Task not found")
			return
		# Update the task description
		task.update_description(description)
		self.tasks.loc[self.tasks['task_id'] == task_id, 'description'] = description
		tdb.update_task_in_db(user_id=self.user_id, task=task)

	def change_day(self, task_id: int, day: str) -> None:
		"""
		Change the day to do the task
		:param task_id: The task ID
		:param day: The new day of the week to do the task
		"""
		# Get Task object
		task = self.get_task_object(task_id)
		if task is None:
			logging.error("Task not found")
			return
		# Update the task day
		task.change_day(day)
		self.tasks.loc[self.tasks['task_id'] == task_id, 'day'] = day
		tdb.update_task_in_db(user_id=self.user_id, task=task)

	def change_course_name(self, task_id: int, course_name: str) -> None:
		"""
		Change the course name of a task
		:param task_id: The task ID
		:param course_name: The new course name
		"""
		# Get Task object
		task = self.get_task_object(task_id)
		if task is None:
			logging.error("Task not found")
			return
		# Update the task course name
		task.update_course_name(course_name)
		self.tasks.loc[self.tasks['task_id'] == task_id, 'course_name'] = course_name
		tdb.update_task_in_db(user_id=self.user_id, task=task)

	def update_deadline_date(self, task_id: int, deadline: bool, deadline_date: datetime.date) -> None:
		"""
		Update the deadline date of a task
		:param deadline: Is there a deadline or not
		:param task_id: The task ID
		:param deadline_date: The new deadline date if there is one
		"""
		# Get Task object
		task = self.get_task_object(task_id)
		if task is None:
			logging.error("Task not found")
			return
		# Update the task deadline date
		task.update_deadline(deadline=deadline, date=deadline_date)
		self.tasks.loc[self.tasks['task_id'] == task_id, 'deadline_date'] = deadline_date
		self.tasks.loc[self.tasks['task_id'] == task_id, 'deadline'] = deadline
		tdb.update_task_in_db(user_id=self.user_id, task=task)

	def remove_task(self, task_id: int) -> None:
		"""
		Remove a task from the list
		:param task_id: The task ID
		"""
		self.tasks = self.tasks[self.tasks['task_id'] != task_id]
		tdb.remove_task_from_db(user_id=self.user_id, task_id=task_id)
