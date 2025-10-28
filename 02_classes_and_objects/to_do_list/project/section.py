from project.task import Task


class Section:
	def __init__(self, name: str):
		self.name = name
		self.tasks: list[Task] = []
	
	def add_task(self, new_task: Task) -> str:
		searched_task = next((t for t in self.tasks if t.name == new_task.name),
			None)
		
		if searched_task:
			return f"Task is already in the section {self.name}"
		
		self.tasks.append(new_task)
		return f"Task {new_task.details()} is added to the section"
	
	def complete_task(self, task_name: str) -> str:
		searched_task = next((t for t in self.tasks if t.name == task_name),
			None)
		
		if not searched_task:
			return f"Could not find task with the name {task_name}"
		
		searched_task.completed = True
		return f"Completed task {task_name}"
	
	def clean_section(self):
		total_tasks = len(self.tasks)
		self.tasks = [t for t in self.tasks if t.completed != True]
		
		return f"Cleared {total_tasks - len(self.tasks)} tasks."
	
	def view_section(self):
		output = [f"Section {self.name}:"]
		for task in self.tasks:
			output.append(task.details())
		
		return '\n'.join(output)
