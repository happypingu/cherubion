from . import interface

RACES = ["eemsi", "keor", "hreeir", "azen", "hhrgak"]

# TODO: add relevant data
def create_race():
    interface.print_("There are five races you can choose from: Eemsi, Keor, Hreeir, Azen, Hhrgak\n")
    interface.print_("if u wanna see the info, say info and the name of the race")
    interface.print_("if u wanna choose say choose and the name of the race")

    while True:
        choose_or_info = input()
        info_choose_commands = ['info eemsi', 'info keor', 'info hreeir', 'info azen', 'info hhrgak', 'choose eemsi', 'choose keor', 'choose hreeir', 'choose azen', 'choose hhrgak']
        if choose_or_info.lower() == info_choose_commands[0]:
            interface.print_()
            interface.print_('Race: Eemsi')
            interface.print_('Health:', 26)
            interface.print_('Strength:', 17)
            interface.print_('Defence:', 14)
            interface.print_('Luck:', 7)
            interface.print_('Magic:', 20)
            interface.print_()

        if choose_or_info.lower() == info_choose_commands[1]:
            interface.print_()
            interface.print_('Race: Keor')
            interface.print_('Health:', 28)
            interface.print_('Strength:', 11)
            interface.print_('Defence:', 16)
            interface.print_('Luck:', 9)
            interface.print_('Magic:', 20)
            interface.print_()

        if choose_or_info.lower() == info_choose_commands[2]:
            interface.print_()
            interface.print_('Race: Hreeir')
            interface.print_('Health:', 24)
            interface.print_('Strength:', 14)
            interface.print_('Defence:', 14)
            interface.print_('Luck:', 8)
            interface.print_('Magic:', 20)
            interface.print_()

        if choose_or_info.lower() == info_choose_commands[3]:
            interface.print_()
            interface.print_('Race: Azen')
            interface.print_('Health:', 16)
            interface.print_('Strength:', 14)
            interface.print_('Defence:', 14)
            interface.print_('Luck:', 11)
            interface.print_('Magic:', 25)
            interface.print_()

        if choose_or_info.lower() == info_choose_commands[4]:
            interface.print_()
            interface.print_('Race: Hhrgak')
            interface.print_('Health:', 18)
            interface.print_('Strength:', 11)
            interface.print_('Defence:', 15)
            interface.print_('Luck:', 11)
            interface.print_('Magic:', 28)
            interface.print_()


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


# TODO: add relevant data
def datadict(self):
    return {
        'Race': str(self.ourrace),
        'Health': str(self.health),
        'Strength': str(self.strength),
        'Defence': str(self.defence),
        'Luck': str(self.luck),
        'Magic': str(self.magic)
    }


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


# TODO: add relevant data
def print_info(self):
    interface.print_('Race', str(self.ourrace))
    interface.print_('Health', str(self.health))
    interface.print_('Strength', str(self.strength))
    interface.print_('Defence', str(self.defence))
    interface.print_('Luck', str(self.luck))
    interface.print_('Magic', str(self.magic))