from project.room import Room


class Hotel:
	def __init__(self, name: str):
		self.name = name
		self.rooms: list[Room] = []
	
	@property
	def guests(self) -> int:
		return sum([room.guests for room in self.rooms])
	
	@classmethod
	def from_stars(cls, stars_count: int):
		return cls(f"{stars_count} stars Hotel")
	
	def add_room(self, room: Room):
		self.rooms.append(room)
	
	def take_room(self, room_number: int, people: int) -> str | None:
		searched_room = [r for r in self.rooms if r.number == room_number][0]
		return searched_room.take_room(people)
	
	def free_room(self, room_number: int) -> str | None:
		searched_room = [r for r in self.rooms if r.number == room_number][0]
		return searched_room.free_room()
	
	def status(self) -> str:
		taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
		free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
		return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(free_rooms)}\nTaken rooms: {', '.join(taken_rooms)}"
