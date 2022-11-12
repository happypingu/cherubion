"""
This modules handles the interface and the logic behind creating the player's
character.
"""
from . import interface
from .combat_entity import CombatEntity
from .player import Player
from . import attack

_ENTITY_DISPLAY_NAME = "You"

_EEMSI = "eemsi"
_KEOR = "keor"
_HREEIR = "hreeir"
_AZEN = "azen"
_HHRGAK = "hhrgak"
_RACES = [_EEMSI, _KEOR, _HREEIR, _AZEN, _HHRGAK]

'''
INFO: DMG TEMPLATE
_PUNCH_ATTACK = attack.Attack(
    name="punch",
    display_name="Punch",
    type_=attack.MELEE,
    damage=1,
    stamina_cost=2,
    description_of_being_used="punch"
)
'''
# DEFAULT HP: 20
# DEFAULT STRENGTH: 14
# DEFAULT DEFENCE: 14
# DEFAULT LUCK: 9 || REMOVE 1 LUCK AFTER EVERY USE
# ABILITY POWER: 20 || RESTORE DEFAULT AP AFTER REST

_EEMSI_ENTITY = CombatEntity(
    display_name=_ENTITY_DISPLAY_NAME,
    maximum_health=26,
    strength=17,
    defence=14,
    luck=7,
    magic=20,
)

_KEOR_ENTITY = CombatEntity(
    display_name=_ENTITY_DISPLAY_NAME,
    maximum_health=28,
    strength=11,
    defence=16,
    luck=9,
    magic=20,
)

_HREEIR_ENTITY = CombatEntity(
    display_name=_ENTITY_DISPLAY_NAME,
    maximum_health=24,
    strength=14,
    defence=14,
    luck=8,
    magic=20,
)

_AZEN_ENTITY = CombatEntity(
    display_name=_ENTITY_DISPLAY_NAME,
    maximum_health=16,
    strength=14,
    defence=14,
    luck=11,
    magic=25,
)

_HHRGAK_ENTITY = CombatEntity(
    display_name=_ENTITY_DISPLAY_NAME,
    maximum_health=18,
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
