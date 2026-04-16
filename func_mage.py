#!/usr/bin/env python3

"""
FuncMage - Interactive Test Runner
Run this file to test your exercises interactively.
Usage: python3 func_mage.py
"""


# ----------------------------------------------------------------------------
#  Colors
# ----------------------------------------------------------------------------

def color(code: int, text: str) -> str:
    """A function making strings of text colorful."""
    colors: dict = {
            0: "\033[0m",     # Reset
            1: "\033[1;91m",  # Red
            2: "\033[1;92m",  # Green
            3: "\033[1;93m",  # Yellow
            4: "\033[1;94m",  # Blue
            5: "\033[1;95m",  # Magenta
            6: "\033[1;96m",  # Cyan
            7: "\033[1;97m"   # White
        }

    if code < 7:
        color = colors[code]
    else:
        color = colors[7]

    return f'{color}{text}{colors[0]}'


# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

import os
import sys
import random
from enum import Enum
from typing import List, Dict, Any


def pathfinder(folder_name: str) -> None:
    """Adds the specified exercise folder to the Python path."""
    folder_path = os.path.join(os.path.dirname(__file__), folder_name)
    if folder_path not in sys.path:
        sys.path.insert(0, folder_path)


FOLDERS: list = ['ex0', 'ex1', 'ex2', 'ex3' 'ex4']
for F in FOLDERS:
    try:
        pathfinder(F)
    except ImportError as e:
        print(f' ERROR! Could not import  {F} — {e}')

from lambda_spells import artifact_sorter
from lambda_spells import power_filter
from lambda_spells import spell_transformer
from lambda_spells import mage_stats


# ----------------------------------------------------------------------------
#  Enums
# ----------------------------------------------------------------------------

class MageNames(str, Enum):
    ALEX = "Alex"
    JORDAN = "Jordan"
    RILEY = "Riley"
    CASEY = "Casey"
    MORGAN = "Morgan"
    SAGE = "Sage"
    RIVER = "River"
    PHOENIX = "Phoenix"
    EMBER = "Ember"
    STORM = "Storm"
    LUNA = "Luna"
    NOVA = "Nova"
    ZARA = "Zara"
    KAI = "Kai"
    ROWAN = "Rowan"
    ASH = "Ash"


class Elements(str, Enum):
    FIRE = "fire"
    ICE = "ice"
    LIGHTNING = "lightning"
    EARTH = "earth"
    WIND = "wind"
    WATER = "water"
    LIGHT = "light"
    SHADOW = "shadow"


class SpellNames(str, Enum):
    FIREBALL = "fireball"
    HEAL = "heal"
    SHIELD = "shield"
    LIGHTNING = "lightning"
    FREEZE = "freeze"
    EARTHQUAKE = "earthquake"
    TORNADO = "tornado"
    TSUNAMI = "tsunami"
    FLASH = "flash"
    DARKNESS = "darkness"
    METEOR = "meteor"
    BLIZZARD = "blizzard"


class ArtifactNames(str, Enum):
    CRYSTAL_ORB = "Crystal Orb"
    FIRE_STAFF = "Fire Staff"
    ICE_WAND = "Ice Wand"
    LIGHTNING_ROD = "Lightning Rod"
    EARTH_SHIELD = "Earth Shield"
    WIND_CLOAK = "Wind Cloak"
    WATER_CHALICE = "Water Chalice"
    SHADOW_BLADE = "Shadow Blade"
    LIGHT_PRISM = "Light Prism"
    STORM_CROWN = "Storm Crown"


class ArtifactTypes(str, Enum):
    WEAPON = "weapon"
    FOCUS = "focus"
    ARMOR = "armor"
    ACCESSORY = "accessory"
    RELIC = "relic"


class EnchantmentTypes(str, Enum):
    FLAMING = "Flaming"
    FROZEN = "Frozen"
    SHOCKING = "Shocking"
    EARTHEN = "Earthen"
    WINDY = "Windy"
    FLOWING = "Flowing"
    RADIANT = "Radiant"
    DARK = "Dark"


class Items(str, Enum):
    SWORD = "Sword"
    SHIELD = "Shield"
    STAFF = "Staff"
    WAND = "Wand"
    ARMOR = "Armor"
    RING = "Ring"
    AMULET = "Amulet"
    CLOAK = "Cloak"


# ----------------------------------------------------------------------------
#  Generators
# ----------------------------------------------------------------------------

def generate_mages(count: int) -> List[Dict[str, Any]]:
    """Generate a list of mages with random attributes."""
    mages = []
    for _ in range(count):
        mage = {
            'name': random.choice(list(MageNames)),
            'power': random.randint(50, 100),
            'element': random.choice(list(Elements))
        }
        mages.append(mage)
        return mages


def generate_artifacts(count: int) -> List[Dict[str, Any]]:
    """Generate a list of magical artifacts."""
    artifacts = []
    for _ in range(count):
        artifact = {
            'name': random.choice(list(ArtifactNames)),
            'power': random.randint(60, 120),
            'type': random.choice(list(ArtifactTypes))
        }
        artifacts.append(artifact)
    return artifacts


def generate_spells(count: int) -> List[str]:
    """Generate a list of spell names."""
    return random.sample(SpellNames, min(count, len(list(SpellNames))))


def generate_spell_powers(count: int) -> List[int]:
    """Generate a list of spell power values."""
    return [random.randint(10, 50) for _ in range(count)]


def generate_enchantment_items(count: int) -> List[str]:
    """Generate a list of items to be enchanted."""
    return random.sample(Items, min(count, len(Items)))


# ----------------------------------------------------------------------------
#  Exercise 0: Lambda Sanctum
# ----------------------------------------------------------------------------

class LambdaSanctum():

    def __init__(self) -> None:
        self._artifacts = generate_artifacts(random.randint(5, 10))
        self._mages = generate_mages(random.randint(5, 10))
        self._spells = generate_spells((random.randint(5, 10))

    def run_test(self) -> None:

        try:

            print()
            print(" " + "-" * 60)
            print(color(7, ' 💫 Exercise 0: Lambda Sanctum'))
            print(" " + "-" * 60)

            print()
            print(color(6, ' Testing Valid Station'))
            print(" " + "-" * 60)

    sorted_artifacts = artifact_sorter(artifacts)

    # --- Test power_filter()

    # --- Test spell_transformer()

    # --- Test mage_stats()

# ----------------------------------------------------------------------------
#  FuncMage Chronicles
# ----------------------------------------------------------------------------

def func_mage() -> None:
    """Interactive UI."""
        print()
        print(" " + "-" * 60)
        print(color(3, ' 🪄 WELCOME FUNC MAGE!'))
        print(" " + "-" * 60)
        print(" This program will help you test the exercises of this module.")
        print(" Which exercise would you like to test?")

        print()
        print(color(7, f" {'n.':<5}{'Exercise':<30}{'Description'}"))
        print(" " + "-" * 60)
        print(f" {'0':<5}{'Lambda Sanctum':<30}"
              "...")
        print(f" {'1':<5}{'Higher Realm':<30}"
              "...")
        print(f" {'2':<5}{'Memory Depths':<30}"
              "...")
        print(f" {'3':<5}{'Ancient Library':<30}"
              "...")
        print(f" {'4':<5}{'Master’s Tower':<30}"
              "...")

        print()
        choice = input(color(3, ' 🪄 Enter your choice (0/1/2/3/4): '))

        if choice == "0":
            lambda_sanctum()
        elif choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        else:
            print(color(5, ' ERROR! Invalid choice! Please enter 0, 1, 2, 3, or 4'))


if __name__ == "__main__":
    func_mage()
