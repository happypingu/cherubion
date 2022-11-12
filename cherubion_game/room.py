class Room:
    def __init__(self, enter):
        self.enter_function = enter
        self.has_been_entered_before = False

    def enter(self, player):
        self.enter_function(self, player)
