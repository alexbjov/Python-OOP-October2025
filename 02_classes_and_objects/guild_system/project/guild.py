from project.player import Player


class Guild:
	def __init__(self, name: str):
		self.name = name
		self.players: list[Player] = []
	
	def assign_player(self, player: Player) -> str:
		if player.guild == "Unaffiliated":
			player.guild = self.name
			self.players.append(player)
			return f"Welcome player {player.name} to the guild {player.guild}"
		
		elif player.guild == self.name:
			return f"Player {player.name} is already in the guild."
		
		return f"Player {player.name} is in another guild."
	
	def kick_player(self, player_name: str) -> str:
		searched_player = next(
			(p for p in self.players if p.name == player_name), None)
		
		if searched_player:
			self.players.remove(searched_player)
			searched_player.guild = "Unaffiliated"
			return f"Player {player_name} has been removed from the guild."
		
		return f"Player {player_name} is not in the guild."
	
	def guild_info(self) -> str:
		output: list[str] = [f"Guild: {self.name}"]
		for player in self.players:
			output.append(player.player_info())
		
		return '\n'.join(output)
