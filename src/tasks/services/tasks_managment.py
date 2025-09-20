from datetime import datetime
from src.tasks.models.Task import Task
import src.tasks.database.tasks_db as tdb
import logging

# TODO: Make logging more meaningful - log the actual changes


class Tasks:
	"""
	This class represents tasks for a specific user.
	Attributes:
		user_id (int): The user's ID
	"""
	user_id: int = None

	def __init__(self, user_id: int) -> None:
		"""
		Initialize the Tasks class with the user ID and load the tasks from the database
		:param user_id: User's ID
		"""
		self.user_id = user_id

	def add_task(self, description: str, course_name: str, day: str, deadline_date: datetime.date,
				 status: bool = False, deadline: bool = False) -> None:
		"""
		Add a new task to be done
		:param description: The task description
		:param course_name: The name of the course the task is for
		:param day: The day of the week to do the task
		:param deadline_date: The task date of submission
		:param status: Is the task done or not
		:param deadline: Does the task have a deadline or not
		"""
		# Create a new Task object
		task = Task(
			course_name=course_name,
			day=day,
			description=description,
			deadline=deadline,
			deadline_date=deadline_date,
			status=status,
			time_completed=None
		)
		# Add the task to the database
		task_id = tdb.add_new_task_to_db(user_id=self.user_id, task=task)
		task.update_task_id(task_id)
		logging.debug(f"Task {task.task_id} added to the database")

	def complete_task(self, task_id: int) -> None:
		"""
		Mark the task as completed
		:param task_id: The task ID
		"""
		task = tdb.get_task_from_db(user_id=self.user_id, task_id=task_id)
		if task is None:
			logging.error("Task not found")
			return
		# Update the task status
		task.mark_complete()
		# Update the task in the database
		tdb.update_task_in_db(user_id=self.user_id, task=task)
		logging.debug(f"Task {task.task_id} marked as completed in the database")

	def change_description(self, task_id: int, description: str) -> None:
		"""
		Change the description of a task
		:param task_id: The task ID
		:param description: The new task description
		"""
		# Get Task object
		task = tdb.get_task_from_db(user_id=self.user_id, task_id=task_id)
		if task is None:
			logging.error("Task not found")
			return
		# Update the task description
		task.update_description(description)
		# Update the task in the database
		tdb.update_task_in_db(user_id=self.user_id, task=task)
		logging.debug(f"Task {task.task_id} description updated in the database")

	def change_day(self, task_id: int, day: str) -> None:
		"""
		Change the day to do the task
		:param task_id: The task ID
		:param day: The new day of the week to do the task
		"""
		# Get Task object
		task = tdb.get_task_from_db(user_id=self.user_id, task_id=task_id)
		if task is None:
			logging.error("Task not found")
			return
		# Update the task description
		task.change_day(day)
		tdb.update_task_in_db(user_id=self.user_id, task=task)
		logging.debug(f"Task {task.task_id} day updated in the database")

	def change_course_name(self, task_id: int, course_name: str) -> None:
		"""
		Change the course name of a task
		:param task_id: The task ID
		:param course_name: The new course name
		"""
		# Get Task object
		task = tdb.get_task_from_db(user_id=self.user_id, task_id=task_id)
		if task is None:
			logging.error("Task not found")
			return
		# Update the task description
		task.update_course_name(course_name)
		# Update the task in the database
		tdb.update_task_in_db(user_id=self.user_id, task=task)
		logging.debug(f"Task {task.task_id} course name updated in the database")

	def update_deadline_date(self, task_id: int, deadline: bool, deadline_date: datetime.date) -> None:
		"""
		Update the deadline date of a task
		:param deadline: Is there a deadline or not
		:param task_id: The task ID
		:param deadline_date: The new deadline date if there is one
		"""
		# Get Task object
		task = tdb.get_task_from_db(user_id=self.user_id, task_id=task_id)
		if task is None:
			logging.error("Task not found")
			return
		# Update the task description
		task.update_deadline(deadline=deadline, date=deadline_date)
		# Update the task in the database
		tdb.update_task_in_db(user_id=self.user_id, task=task)
		logging.debug(f"Task {task.task_id} deadline date updated in the database")

	def remove_task(self, task_id: int) -> None:
		"""
		Remove a task from the list
		:param task_id: The task ID
		"""
		tdb.remove_task_from_db(user_id=self.user_id, task_id=task_id)
		logging.debug(f"Task {task_id} removed from the database")
