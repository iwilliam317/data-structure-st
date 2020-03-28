import pyhash 

class Pokedex():
    def __init__(self):
        self.big_vector = [0]*20
        self.fnv = pyhash.fnv1_32()
        self.murmur = pyhash.murmur3_32()

    def add_pokemon(self, pokemon):
        fnv_pokemon = self.fnv(pokemon)%20
        murmur_pokemon = self.murmur(pokemon)%20

        if self.is_pokemon_saved(fnv_pokemon, murmur_pokemon):
            print('already got %s!' %(pokemon))
            return

        self.big_vector[fnv_pokemon] = 1
        self.big_vector[murmur_pokemon] = 1
        print('added %s' %(pokemon))

    def is_pokemon_saved(self, fnv_pokemon, murmur_pokemon):
        return (self.big_vector[fnv_pokemon] & self.big_vector[murmur_pokemon])
pokedex = Pokedex()
pokedex.add_pokemon('pikachu')
pokedex.add_pokemon('charmander')
pokedex.add_pokemon('pikachu')
pokedex.add_pokemon('pikachu')
pokedex.add_pokemon('charmander')
