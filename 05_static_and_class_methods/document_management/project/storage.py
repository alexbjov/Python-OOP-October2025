from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
	def __init__(self):
		self.categories: list[Category] = []
		self.topics: list[Topic] = []
		self.documents: list[Document] = []
	
	def add_category(self, category: Category) -> None:
		if category not in self.categories:
			self.categories.append(category)
	
	def add_topic(self, topic: Topic) -> None:
		if topic not in self.topics:
			self.topics.append(topic)
	
	def add_document(self, document: Document) -> None:
		if document not in self.documents:
			self.documents.append(document)
	
	def edit_category(self, category_id: int, new_name: str) -> None:
		searched_category = next(
			(cat for cat in self.categories if cat.id == category_id), None)
		searched_category.edit(new_name)
	
	def edit_topic(self, topic_id: int, new_topic: str,
			new_storage_folder: str) -> None:
		searched_topic = next((t for t in self.topics if t.id == topic_id),
			None)
		searched_topic.edit(new_topic, new_storage_folder)
	
	def edit_document(self, document_id: int, new_file_name: str) -> None:
		searched_doc = next((d for d in self.documents if d.id == document_id),
			None)
		searched_doc.edit(new_file_name)
	
	def delete_category(self, category_id) -> None:
		searched_category = next(
			(cat for cat in self.categories if cat.id == category_id), None)
		if searched_category:
			self.categories.remove(searched_category)
	
	def delete_topic(self, topic_id) -> None:
		searched_topic = next((t for t in self.topics if t.id == topic_id),
			None)
		if searched_topic:
			self.topics.remove(searched_topic)
	
	def delete_document(self, document_id) -> None:
		searched_doc = next((d for d in self.documents if d.id == document_id),
			None)
		if searched_doc:
			self.documents.remove(searched_doc)
	
	def get_document(self, document_id: int) -> Document | None:
		return next((d for d in self.documents if d.id == document_id), None)
	
	def __repr__(self):
		result = []
		for doc in self.documents:
			result.append(repr(doc))
		
		return "\n".join(result)
