from cherubion_game import interface

RACES = ["eemsi", "keor", "hreeir", "azen", "hhrgak"]

race_info = {
        "eemsi": {
            "health": 26,
            "strength": 17,
            "defence": 14,
            "luck": 7,
            "magic": 20
        },
        "keor": {
            "health": 28,
            "strength": 11,
            "defence": 16,
            "luck": 9,
            "magic": 20
        },
        "hreeir": {
            "health": 24,
            "strength": 14,
            "defence": 14,
            "luck": 8,
            "magic": 20
        },
        "azen": {
            "health": 16,
            "strength": 14,
            "defence": 14,
            "luck": 11,
            "magic": 28
        },
        "hhrgak": {
            "health": 18,
            "strength": 11,
            "defence": 15,
            "luck": 11,
            "magic": 28
        },
    }

def create_race():
    commands = ["info " + race for race in RACES] + ["choose " + race for race in RACES]

    interface.print_("There are five races you can choose from: Eemsi, Keor, Hreeir, Azen, Hhrgak\n")
    interface.print_("To see information about a race, enter 'info' followed by the name of the race.")
    interface.print_("To choose a race, enter 'choose' followed by the name of the race.\n")

    while True:
        user_input = input("> ")
        
        for race in RACES:
            if user_input.lower() == f"info {race}":
                interface.print_()
                interface.print_(f'Race: {race.capitalize()}')
                interface.print_(f'Health: {race_info[race]["health"]}')
                interface.print_(f'Strength: {race_info[race]["strength"]}')
                interface.print_(f'Defence: {race_info[race]["defence"]}')
                interface.print_(f'Luck: {race_info[race]["luck"]}')
                interface.print_(f'Magic: {race_info[race]["magic"]}')
                interface.print_()

            elif f"choose {race}" in user_input.lower():
                player = Hero(race)
                return player
            

        if user_input.lower() not in commands:
            print('Not a valid command!')


class Hero:
    def __init__(self, herorace):
        self.ourrace = herorace

        self.basehealth = race_info[self.ourrace]["health"]
        self.health = self.basehealth

        self.basestrength = race_info[self.ourrace]["strength"]
        self.strength = self.basestrength

        self.basedefence = race_info[self.ourrace]["defence"]
        self.defence = self.basedefence

        self.baseluck = race_info[self.ourrace]["luck"]
        self.luck = self.baseluck

        self.basemagic = race_info[self.ourrace]["magic"]
        self.magic = self.basemagic
    
    def __str__(self):
        return (
            f"Race: {self.ourrace.capitalize()}\n"
            f"Health: {self.health}\n"
            f"Strength: {self.strength}\n"
            f"Defence: {self.defence}\n"
            f"Luck: {self.luck}\n"
            f"Magic: {self.magic}\n"
        )