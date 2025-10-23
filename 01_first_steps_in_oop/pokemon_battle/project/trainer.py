from project.pokemon import Pokemon


class Trainer:
	def __init__(self, name: str):
		self.name = name
		self.pokemons: list[Pokemon] = []
	
	def add_pokemon(self, pokemon: Pokemon):
		if pokemon in self.pokemons:
			return f"This pokemon is already caught"
		
		self.pokemons.append(pokemon)
		return f"Caught {pokemon.pokemon_details()}"
	
	def release_pokemon(self, pokemon_name: str):
		searched_pokemon = next(
			(p for p in self.pokemons if p.name == pokemon_name), None)
		
		if searched_pokemon:
			self.pokemons.remove(searched_pokemon)
			return f"You have released {pokemon_name}"
		
		return f"Pokemon is not caught"
	
	def trainer_data(self) -> str:
		output = [
			f"Pokemon Trainer {self.name}",
			f"Pokemon count {len(self.pokemons)}"
		]
		
		if self.pokemons:
			for pokemon in self.pokemons:
				output.append(f"- {pokemon.pokemon_details()}")
		
		return '\n'.join(output)
