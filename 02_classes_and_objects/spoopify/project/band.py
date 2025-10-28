from project.album import Album


class Band:
	def __init__(self, name: str):
		self.name = name
		self.albums: list[Album] = []
	
	def add_album(self, album: Album) -> str:
		searched_album = next(
			(alb for alb in self.albums if alb.name == album.name), None)
		
		if searched_album:
			return f"Band {self.name} already has {album.name} in their library."
		
		self.albums.append(album)
		return f"Band {self.name} has added their newest album {album.name}."
	
	def remove_album(self, album_name: str) -> str:
		searched_album = next(
			(alb for alb in self.albums if alb.name == album_name), None)
		
		if not searched_album:
			return f"Album {album_name} is not found."
		
		elif searched_album.published:
			return f"Album has been published. It cannot be removed."
		
		self.albums.remove(searched_album)
		return f"Album {album_name} has been removed."
	
	def details(self) -> str:
		output = [f"Band {self.name}"]
		for album in self.albums:
			output.append(album.details())
		
		return '\n'.join(output)
