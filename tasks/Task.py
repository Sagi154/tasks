from datetime import datetime
from dataclasses import dataclass, field

days_hebrew = {
	"Sunday": "ראשון",
	"Monday": "שני",
	"Tuesday": "שלישי",
	"Wednesday": "רביעי",
	"Thursday": "חמישי",
	"Friday": "שישי",
	"Saturday": "שבת"
}

active_courses = {
	"InfoSec": "מבוא לאבטחת מידע",
	"Optimization": "מבוא לאופטימיזציה למדעי ה מחשב",
	"Statistics": "סטטיסטיקה למדעי המחשב",
	"Robot Seminar": "סמינר רובוטים",
	"Projects": "פרוייקטים"
}


@dataclass
class Task:
	"""
	This dataclass represents a task

	Attributes:
		task_id (int): The task ID
		course_name (str): The name of the course the task is for.
		day (str): The day of the week to do the task.
		description (str): What is the task.
		deadline (bool): Does the task have a deadline or not.
		deadline_date (datetime.date): The task date of submission.
		time_created (datetime.date): The time the task is created.
		status (bool): Is the task done or not.
		time_completed (datetime.date): The time when the task was completed.
	"""
	course_name: str
	day: str
	description: str
	deadline_date: datetime.date
	deadline: bool = False
	time_created: datetime.date = field(default_factory=lambda: datetime.now().time())
	status: bool = False
	time_completed: datetime.date = None
	task_id: int = 0

	def __post_init__(self):
		"""
		Post init function to check if the day is valid
		"""
		if self.course_name in active_courses:
			self.course_name = self.course_name
		else:
			self.course_name = None
		if self.day in days_hebrew:
			self.day = self.day
		else:
			self.day = None

		if not self.deadline:
			self.deadline_date = None

	def values(self) -> tuple:
		"""
		:return: A tuple of the 7 parameters of a task
		"""
		return self.course_name, self.day, self.description, self.deadline, self.deadline_date, \
			   self.time_created, self.status, self.time_completed

	def update_task_id(self, task_id: int) -> None:
		"""
		Update the task ID
		:param task_id: The new task ID
		"""
		self.task_id = task_id

	def change_day(self, day: str) -> None:
		"""
		Change the task day

		:param day: The new day of the week
		"""
		self.day = day if day in days_hebrew else 'non_day'

	def update_course_name(self, course_name: str) -> None:
		"""
		Update the course name
		:param course_name: The new course name
		"""
		self.course_name = course_name

	def update_description(self, description: str) -> None:
		"""
		Update the task description
		:param description: The new task description
		"""
		self.description = description

	def update_deadline(self, deadline=True, date: datetime.date = None) -> None:
		"""
		Update task to have a deadline or update the deadline date
		:param deadline: Does the task have a deadline or not
		:param date: The task date of submission
		"""
		self.deadline_date = date
		self.deadline = deadline

	def mark_complete(self) -> None:
		"""
		Mark the task as complete
		"""
		self.status = True
		self.time_completed = datetime.now().date()

	def __str__(self) -> str:
		"""
		TODO: Update later to be more meaningful
		Convert the task to a string
		:return: The task as a string
		"""
		return (f"Task: {self.description}, Course: {self.course_name}, Day: {self.day}, Deadline: {self.deadline}, "
				f"Deadline date: {self.deadline_date}, Time created: {self.time_created}, Status: {self.status}, "
				f"Time completed: {self.time_completed}")


