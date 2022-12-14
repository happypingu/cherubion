import pickle
from ..player import races


def save_game(player):
    race = races.Hero(player.ourrace)
    with open('savefile.dat', 'wb') as f:
        pickle.dump(race, f, protocol=pickle.HIGHEST_PROTOCOL)

def load_game(player):
    race = races.Hero(player.ourrace)
    with open('savefile.dat', 'rb') as f:
        race = pickle.load(f)
