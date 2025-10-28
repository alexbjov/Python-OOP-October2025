from project.song import Song


class Album:
	def __init__(self, name: str, *songs):
		self.name = name
		self.songs: list[Song] = [song for song in songs]
		self.published: bool = False
	
	def add_song(self, song: Song) -> str:
		if self.published:
			return "Cannot add songs. Album is published."
		
		elif song.single:
			return f"Cannot add {song.name}. It's a single"
		
		searched_song = next((s for s in self.songs if s.name == song.name),
			None)
		if searched_song:
			return f"Song is already in the album."
		
		self.songs.append(song)
		return f"Song {song.name} has been added to the album {self.name}."
	
	def remove_song(self, song_name: str) -> str:
		if self.published:
			return "Cannot remove songs. Album is published."
		
		searched_song = next((s for s in self.songs if s.name == song_name),
			None)
		
		if not searched_song:
			return "Song is not in the album."
		
		self.songs.remove(searched_song)
		return f"Removed song {song_name} from album {self.name}."
	
	def publish(self) -> str:
		if self.published:
			return f"Album {self.name} is already published."
		
		self.published = True
		return f"Album {self.name} has been published."
	
	def details(self) -> str:
		output = [f"Album {self.name}"]
		for song in self.songs:
			output.append(f"== {song.get_info()}")
		
		return '\n'.join(output)
