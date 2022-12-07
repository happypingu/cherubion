from cherubion_game import interface

RACES = ["eemsi", "keor", "hreeir", "azen", "hhrgak"]


# TODO: add relevant data
def create_race():
    interface.print_("There are five races you can choose from: Eemsi, Keor, Hreeir, Azen, Hhrgak\n")
    interface.print_("To see information about a race, enter 'info' followed by the name of the race.")
    interface.print_("To choose a race, enter 'choose' followed by the name of the race.\n")

    while True:
        ourclass = input("> ")

        if ourclass.lower() == "info eemsi":
            interface.print_()
            interface.print_('Race: Eemsi')
            interface.print_('Health:', 26)
            interface.print_('Strength:', 17)
            interface.print_('Defence:', 14)
            interface.print_('Luck:', 7)
            interface.print_('Magic:', 20)
            interface.print_()

        if ourclass.lower() == "info keor":
            interface.print_()
            interface.print_('Race: Keor')
            interface.print_('Health:', 28)
            interface.print_('Strength:', 11)
            interface.print_('Defence:', 16)
            interface.print_('Luck:', 9)
            interface.print_('Magic:', 20)
            interface.print_()

        if ourclass.lower() == "info hreeir":
            interface.print_()
            interface.print_('Race: Hreeir')
            interface.print_('Health:', 24)
            interface.print_('Strength:', 14)
            interface.print_('Defence:', 14)
            interface.print_('Luck:', 8)
            interface.print_('Magic:', 20)
            interface.print_()

        if ourclass.lower() == "info azen":
            interface.print_()
            interface.print_('Race: Azen')
            interface.print_('Health:', 16)
            interface.print_('Strength:', 14)
            interface.print_('Defence:', 14)
            interface.print_('Luck:', 11)
            interface.print_('Magic:', 25)
            interface.print_()

        if ourclass.lower() == "info hhrgak":
            interface.print_()
            interface.print_('Race: Hhrgak')
            interface.print_('Health:', 18)
            interface.print_('Strength:', 11)
            interface.print_('Defence:', 15)
            interface.print_('Luck:', 11)
            interface.print_('Magic:', 28)
            interface.print_()

        if ourclass.lower() == "choose eemsi":
            return "eemsi"

        elif ourclass.lower() == "choose keor":
            return "keor"

        elif ourclass.lower() == "choose hreeir":
            return "hreeir"

        elif ourclass.lower() == "choose azen":
            return "azen"

        elif ourclass.lower() == "choose hhrgak":
            return "hhrgak"

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
        if self.ourclass == 'eemsi':
            self.basehealth = 26
            self.basestrength = 17
            self.basedefence = 14
            self.baseluck = 7
            self.basemagic = 20
        
        elif self.ourclass == 'keor':
            self.basehealth = 28
            self.basestrength = 11
            self.basedefence = 16
            self.baseluck = 9
            self.basemagic = 20

        elif self.ourclass == 'hreeir':
            self.basehealth = 24
            self.basestrength = 14
            self.basedefence = 14
            self.baseluck = 8
            self.basemagic = 20

        elif self.ourclass == 'azen':
            self.basehealth = 16
            self.basestrength = 14
            self.basedefence = 14
            self.baseluck = 11
            self.basemagic = 25

        elif self.ourclass == 'hhrgak':
            self.basehealth = 18
            self.basestrength = 11
            self.basedefence = 15
            self.baseluck = 11
            self.basemagic = 28