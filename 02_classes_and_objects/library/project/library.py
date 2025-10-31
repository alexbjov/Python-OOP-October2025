from project.user import User


class Library:
	def __init__(self):
		self.user_records: list[User] = []
		self.books_available: dict[str, list[str]] = {}  # author, book_names
		self.rented_books: dict[
			str, dict[str, int]] = {}  # username, {book_name: days_to_return}
	
	def get_book(self, author: str, book_name: str, days_to_return: int,
			user: User) -> str | None:
		if author in self.books_available and book_name in self.books_available[
			author]:
			self.books_available[author].remove(book_name)
			user.books.append(book_name)
			if user.username not in self.rented_books:
				self.rented_books[user.username] = {}
			self.rented_books[user.username][book_name] = days_to_return
			return f"{book_name} successfully rented for the next {days_to_return} days!"
		
		for username, books in self.rented_books.items():
			if book_name in books:
				days_left = books[book_name]
				return f'The book "{book_name}" is already rented and will be available in {days_left} days!'
	
	def return_book(self, author: str, book_name: str,
			user: User) -> str | None:
		if book_name in user.books:
			user.books.remove(book_name)
			if author not in self.books_available:
				self.books_available[author] = []
			self.books_available[author].append(book_name)
			
			if user.username in self.rented_books and book_name in \
					self.rented_books[user.username]:
				del self.rented_books[user.username][book_name]
			
			return None
		
		return f"{user.username} doesn't have this book in his/her records!"
