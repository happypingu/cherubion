'''
from . import interface
from .player.races import Player

_ENTITY_DISPLAY_NAME = "You"

_EEMSI = "eemsi"
_KEOR = "keor"
_HREEIR = "hreeir"
_AZEN = "azen"
_HHRGAK = "hhrgak"
_RACES = [_EEMSI, _KEOR, _HREEIR, _AZEN, _HHRGAK]

# DEFAULT HP: 20
# DEFAULT STRENGTH: 14
# DEFAULT DEFENCE: 14
# DEFAULT LUCK: 9 || REMOVE 1 LUCK AFTER EVERY USE
# ABILITY POWER: 20 || RESTORE DEFAULT AP AFTER REST

_EEMSI_ENTITY = CombatEntity(
    display_name=_ENTITY_DISPLAY_NAME,
    max_hp=26,
    strength=17,
    defence=14,
    luck=7,
    magic=20,
)

_KEOR_ENTITY = CombatEntity(
    display_name=_ENTITY_DISPLAY_NAME,
    max_hp=28,
    strength=11,
    defence=16,
    luck=9,
    magic=20,
)

_HREEIR_ENTITY = CombatEntity(
    display_name=_ENTITY_DISPLAY_NAME,
    max_hp=24,
    strength=14,
    defence=14,
    luck=8,
    magic=20,
)

_AZEN_ENTITY = CombatEntity(
    display_name=_ENTITY_DISPLAY_NAME,
    max_hp=16,
    strength=14,
    defence=14,
    luck=11,
    magic=25,
)

_HHRGAK_ENTITY = CombatEntity(
    display_name=_ENTITY_DISPLAY_NAME,
    max_hp=18,
    strength=11,
    defence=15,
    luck=11,
    magic=28,
)

def create_player():
    interface.print_multiple_lines([
        "On your adventure you may be an Eemsi, Keor, Hreeir, Azen, or Hhrgak.",
        "Which do you choose?"
    ])

    command = interface.get_command(_RACES)

    interface.print_("You have chosen the race {}.".format(command))
    interface.print_()

    if command == _EEMSI:
        return Player(_EEMSI_ENTITY, "eemsi")

    if command == _KEOR:
        return Player(_KEOR_ENTITY, "keor")

    if command == _HREEIR:
        return Player(_HREEIR_ENTITY, "hreeir")

    if command == _AZEN:
        return Player(_AZEN_ENTITY, "azen")

    if command == _HHRGAK:
        return Player(_HHRGAK_ENTITY, "hhrgak")
'''
RACES = ["eemsi", "keor", "hreeir", "azen", "hhrgak"]

def create_race():
    print("There are five races you can choose from: Eemsi, Keor, Hreeir, Azen, Hhrgak\n")
    print("if u wanna see the info, say info and the name of the race")
    print("if u wanna choose say choose and the name of the race")
    while True:
        choose_or_info = input()

        if choose_or_info.lower() == "info eemsi":
            print(f'Health: {Eemsi.max_health}')


        race_prompt = input()
        if race_prompt.lower() == "eemsi":
            race_chosen = Eemsi.create_player

        if race_prompt.lower() == "keor":
            race_chosen = Keor.create_player

        if race_prompt.lower() == "hreeir":
            race_chosen = Hreeir.create_player

        if race_prompt.lower() == "azen":
            race_chosen = Azen.create_player

        if race_prompt.lower() == "hhrgak":
            race_chosen = Hhrgak.create_player
    
    return race_chosen

class Eemsi():
    def create_player(self):
        self.max_health = 26
        self.health = self.max_health
        self.strength = 17
        self.defence = 14
        self.luck = 7
        self.magic = 20
    
    def show_info():
        print(f'Health: ')
        print(f'Strength: ')
        print(f'Defence: ')
        print(f'Luck: ')
        print(f'Magic: ')

class Keor():
    def create_player(self):
        self.max_health = 28
        self.health = self.max_health
        self.strength = 11
        self.defence = 16
        self.luck = 9
        self.magic = 20


class Hreeir():
    def create_player(self):
        self.max_health = 24
        self.health = self.max_health
        self.strength = 14
        self.defence = 14
        self.luck = 8
        self.magic = 20


class Azen():
    def create_player(self):
        self.max_health = 16
        self.health = self.max_health
        self.strength = 14
        self.defence = 14
        self.luck = 11
        self.magic = 25


class Hhrgak():
    def create_player(self):
        self.max_health = 18
        self.health = self.max_health
        self.strength = 11
        self.defence = 15
        self.luck = 11
        self.magic = 28