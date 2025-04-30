from Task import Task
import pandas as pd


def get_tasks_for_user(user_id: int) -> pd.DataFrame:
	"""
	Get the tasks for a specific user from the database.
	:param user_id: The user ID
	:return: A DataFrame containing the tasks for the user
	"""
	pass


def update_task_in_db(user_id: int, task: Task) -> int:
	"""
	Update the task in the database using the Task object.
	If the task is new, therefore not in the database, add it to the database.
	:param user_id: The ID of the user the task belongs to
	:param task: The task to update
	:return: The task ID in the database
	"""
	pass


def remove_task_from_db(user_id: int, task_id: int) -> None:
	"""
	Remove the task from the database using the task ID.
	:param user_id: The ID of the user the task belongs to
	:param task_id: The ID of the task to remove
	"""
	pass
