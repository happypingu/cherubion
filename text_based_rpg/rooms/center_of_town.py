from .. import interface
from ..util import move
from ..room import Room

def enter(room, player):

    while True:
        interface.get_game_command(player, room, ["move"])

        places_to_move = ["village", "town square"]

        if player.talked_to_cordelia:
            places_to_move.append("shop")

        if player.can_progress_to_mountain:
            places_to_move.append("goneril mountain")

        move_location = move(places_to_move)

        if move_location == "village":
            from .village import room as village
            village.enter(player)

        if move_location == "town square":
            from .town_square import room as town_square
            town_square.enter(player)

        if move_location == "shop":
            from .shop import room as shop
            shop.enter(player)

        if move_location == "goneril mountain":
            from .mountain_exterior import room as mountain_exterior
            mountain_exterior.enter(player)

room = Room(
    enter=enter
)
