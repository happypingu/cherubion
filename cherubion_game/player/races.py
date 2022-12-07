from cherubion_game import interface

RACES = ["eemsi", "keor", "hreeir", "azen", "hhrgak"]


# TODO: add relevant data
def create_race():
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
    
    interface.print_("There are five races you can choose from: Eemsi, Keor, Hreeir, Azen, Hhrgak\n")
    interface.print_("To see information about a race, enter 'info' followed by the name of the race.")
    interface.print_("To choose a race, enter 'choose' followed by the name of the race.\n")

    while True:
        user_input = input("> ")
        
        for race in RACES:
            if user_input.lower() == f"info {race}":
                interface.print_()
                interface.print_('Race: {race.captalize()}')
                interface.print_('Health:', race_info[race]["health"])
                interface.print_('Strength:', race_info[race]["strength"])
                interface.print_('Defence:', race_info[race]["defence"])
                interface.print_('Luck:', race_info[race]["luck"])
                interface.print_('Magic:', race_info[race]["magic"]])
                interface.print_()

            elif f"choose {race}" in user_input.lower():
                return race
            

            else:
                print('Not a valid command!')


class Hero():
    def __init__(self, herorace, herohealth, herostrength, herodefence, heroluck, heromagic):
        self.ourrace = herorace

        self.basehealth = herohealth
        self.health = self.basehealth

        self.basestrength = herostrength
        self.strength = self.basestrength

        self.basedefence = herodefence
        self.defence = self.basedefence

        self.baseluck = heroluck
        self.luck = self.baseluck

        self.basemagic = heromagic
        self.magic = self.basemagic
    
    def __str__(self):
        return (
            f"Race: {self.ourrace}\n"
            f"Health: {self.health}\n"
            f"Strength: {self.strength}\n"
            f"Defence: {self.defence}\n"
            f"Luck: {self.luck}\n"
            f"Magic: {self.magic}\n"
        )

    def raceperks(self):
        if self.ourrace == 'eemsi':
            self.basehealth = 26
            self.basestrength = 17
            self.basedefence = 14
            self.baseluck = 7
            self.basemagic = 20
        
        elif self.ourrace == 'keor':
            self.basehealth = 28
            self.basestrength = 11
            self.basedefence = 16
            self.baseluck = 9
            self.basemagic = 20

        elif self.ourrace == 'hreeir':
            self.basehealth = 24
            self.basestrength = 14
            self.basedefence = 14
            self.baseluck = 8
            self.basemagic = 20

        elif self.ourrace == 'azen':
            self.basehealth = 16
            self.basestrength = 14
            self.basedefence = 14
            self.baseluck = 11
            self.basemagic = 25

        elif self.ourrace == 'hhrgak':
            self.basehealth = 18
            self.basestrength = 11
            self.basedefence = 15
            self.baseluck = 11
            self.basemagic = 28
