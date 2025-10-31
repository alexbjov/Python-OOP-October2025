from project.library import Library
from project.user import User


class Registration:
	@staticmethod
	def add_user(user: User, library: Library) -> str | None:
		searched_user = next(
			(u for u in library.user_records if u.user_id == user.user_id),
			None)
		if not searched_user:
			library.user_records.append(user)
			return None
		
		return f"User with id = {user.user_id} already registered in the library!"
	
	@staticmethod
	def remove_user(user: User, library: Library) -> str | None:
		if user in library.user_records:
			library.user_records.remove(user)
			if user.username in library.rented_books:
				del library.rented_books[user.username]
			return None
		
		return "We could not find such user to remove!"
	
	@staticmethod
	def change_username(user_id: int, new_username: str,
			library: Library) -> str:
		for user in library.user_records:
			if user.user_id == user_id:
				if user.username == new_username:
					return "Please check again the provided username - it should be different than the username used so far!"
				
				old_username = user.username
				user.username = new_username
				
				if old_username in library.rented_books:
					old_rented = library.rented_books.pop(old_username)
					if new_username in library.rented_books:
						library.rented_books[new_username].update(old_rented)
					else:
						library.rented_books[new_username] = old_rented
				
				return f"Username successfully changed to: {new_username} for user id: {user_id}"
		
		return f"There is no user with id = {user_id}!"
