class Room:
    def __init__(self, enter):
        self.enter_function = enter

    def enter(self, player):
        self.enter_function(self, player)
