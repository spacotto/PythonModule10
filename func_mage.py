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
import operator
import functools
from enum import Enum
from typing import List, Dict, Any
from collections.abc import Callable


def pathfinder(folder_name: str) -> None:
    """Adds the specified exercise folder to the Python path."""
    folder_path = os.path.join(os.path.dirname(__file__), folder_name)
    if folder_path not in sys.path:
        sys.path.insert(0, folder_path)


FOLDERS: list = ['ex0', 'ex1', 'ex2', 'ex3', 'ex4']
for F in FOLDERS:
    try:
        pathfinder(F)
    except ImportError as e:
        print(f' ERROR! Could not import  {F} — {e}')

from lambda_spells import (artifact_sorter, power_filter,
                           spell_transformer, mage_stats)

from higher_magic import (spell_combiner, power_amplifier,
                          conditional_caster, spell_sequence)

from scope_mysteries import (mage_counter, spell_accumulator,
                             enchantment_factory, memory_vault)

from functools_artifacts import (spell_reducer, partial_enchanter,
                                 memoized_fibonacci, spell_dispatcher)

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


class SpellFunctions(Enum):
    FIREBALL = ('fireball', 'Fireball burns', '-')
    HEAL = ('heal', 'Heal restores', '+')
    SHIELD = ('shield', 'Shield protects', '+')
    LIGHTNING = ('lightning', 'Lightning shocks', '-')
    FREEZE = ('freeze', 'Freeze damages', '-')
    EARTHQUAKE = ('earthquake', 'Earthquake damages', '-')
    TORNADO = ('tornado', 'Tornado damages', '-')
    TSUNAMI = ('tsunami', 'Tsunami damages', '-')
    FLASH = ('flash', 'Flash blinds', '-')
    DARKNESS = ('darkness', 'Darkness damages', '-')
    METEOR = ('meteor', 'Meteor damages', '-')
    BLIZZARD = ('blizzard', 'Blizzard damages', '-')


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


class Targets(str, Enum):
    DRAGON = "Dragon"
    GOBLIN = "Goblin"
    WIZARD = "Wizard"
    KNIGHT = "Knight"


# ----------------------------------------------------------------------------
#  Helpers
# ----------------------------------------------------------------------------

def generate_mages(count: int) -> List[Dict[str, Any]]:
    """Generate a list of mages with random attributes."""
    mages = []
    for _ in range(count):
        mage = {
            'name': random.choice(list(MageNames)).value,
            'power': random.randint(50, 100),
            'element': random.choice(list(Elements)).value
        }
        mages.append(mage)
    return mages


def generate_artifacts(count: int) -> List[Dict[str, Any]]:
    """Generate a list of magical artifacts."""
    artifacts = []
    for _ in range(count):
        artifact = {
            'name': random.choice(list(ArtifactNames)).value,
            'power': random.randint(60, 120),
            'type': random.choice(list(ArtifactTypes)).value
        }
        artifacts.append(artifact)
    return artifacts


def generate_spells(count: int) -> List[str]:
    """Generate a list of spell names."""
    spells = []
    for _ in range(count):
        spells.append(random.choice(list(SpellNames)).value)
    return spells


def generate_spell_function() -> Callable:
    """Generate a function composed by random elemnts."""
    fn_name, effect, mod = random.choice(list(SpellFunctions)).value
    def fn_name(target: str, power: int) -> str:
        return f'{effect} {target}: {mod}{power} HP'
    return fn_name


def valid_cast(target: str, power: int) -> bool:
    """Checks if """
    valid_targets = [target.value for target in Targets]
    if target not in valid_targets:
        return False
    if power < 1:
        return False
    return True


def base_enchantment(power: int, element: str, target: str) -> str:
    return f'{target} enchanted into {element} {target} (+{power} power)'


def generate_spell_dispatcher(count: int) -> List[Any]:
    to_dispatch: List[Any] = []

    for _ in range(count):
        rc = random.choice(['int', 'str', 'list'])
        if rc == 'int':
            item = random.randint(1, 100)
        elif rc == 'str':
            item = random.choice(list(SpellNames)).value
        else:
            item = generate_spells(random.randint(3, 30))
        to_dispatch.append(item)

    to_dispatch.append(None)
    return to_dispatch

# ----------------------------------------------------------------------------
#  Exercise 0: Lambda Sanctum
# ----------------------------------------------------------------------------

class LambdaSanctum():

    def __init__(self) -> None:
        self._artifacts = generate_artifacts(random.randint(5, 10))
        self._mages = generate_mages(random.randint(5, 10))
        self._spells = generate_spells(random.randint(5, 10))

    def run_test(self) -> None:

        print()
        print(" " + "-" * 60)
        print(color(7, ' 🪄 Exercise 0: Lambda Sanctum'))
        print(" " + "-" * 60)

        tests = [('Sorting artifacts', self._run_artifact_sorter),
                  ('Filtering power', self._run_power_filter),
                  ('Transforming spells', self._run_spell_transformer),
                  ('Analysing mages', self._run_mage_stats)]

        for test in tests:
            print()
            print(color(3, f' {test[0]}...'))
            print(" " + "-" * 60)
            test[1]()

        print()

    def _run_artifact_sorter(self) -> None:
        sorted_artifacts = artifact_sorter(self._artifacts)
        print(color(7, f' {"n.":<5}{"Before sort":<25}After sort'))
        print(" " + "-" * 60)

        for idx in range(len(self._artifacts)):
            n = str(idx + 1)

            bn = self._artifacts[idx]['name']
            bp = self._artifacts[idx]['power']
            before = f"[{bp:03}] {bn}"

            an = sorted_artifacts[idx]['name']
            ap = sorted_artifacts[idx]['power']
            after = f"[{ap:03}] {an}"

            print(f' {color(7, f"{n:<4}")} {before:<25}{after}')


    def _run_power_filter(self) -> None:
        filt_pow = power_filter(self._mages, random.randint(75, 100))
        print(color(7, f' {"n.":<5}{"Before filter":<25}After filter'))
        print(" " + "-" * 60)

        for idx in range(len(self._mages)):
            n = str(idx +1)

            bn = self._mages[idx]['name']
            bp = self._mages[idx]['power']
            before = f"[{bp:03}] {bn}"

            if idx < len(filt_pow):
                an = filt_pow[idx]['name']
                ap = filt_pow[idx]['power']
                after = f"[{ap:03}] {an}"
            else:
                after = "-"

            print(f' {color(7, f"{n:<4}")} {before:<25}{after}')


    def _run_spell_transformer(self) -> None:
        trans_spells = spell_transformer(self._spells)
        print(color(7, f' {"n.":<5}{"Before transformation":<25}After transformation'))
        print(" " + "-" * 60)

        for idx in range(len(self._spells)):
            n = str(idx + 1)
            before = self._spells[idx]
            after = trans_spells[idx]

            print(f' {color(7, f"{n:<4}")} {before:<25}{after}')

    def _run_mage_stats(self) -> None:
        ms = mage_stats(self._mages)

        for idx in range(len(self._mages)):
            n = str(idx + 1)
            mage = color(7, f"{n}. {self._mages[idx]['name']}")
            power = f"{self._mages[idx]['power']}"
            print(f" {mage:<27}{power}")

        print(" " + "-" * 60)
        print(f' {color(7, "Maximum Power"):<27}{ms["max_power"]}')
        print(f' {color(7, "Minimum Power"):<27}{ms["min_power"]}')
        print(f' {color(7, "Average Power"):<27}{ms["avg_power"]:.1f}')


# ----------------------------------------------------------------------------
#  Exercise 1: Higher Realm
# ----------------------------------------------------------------------------

class HigherRealm():

    def __init__(self) -> None:
        pass

    def run_test(self) -> None:

        print()
        print(" " + "-" * 60)
        print(color(7, ' 🪄 Exercise 1: Higher Realm'))
        print(" " + "-" * 60)

        tests = [('Combining spells', self._run_spell_combiner),
                  ('Amplifying power', self._run_power_amplifier),
                  ('Casting conditionally', self._run_conditional_caster),
                  ('Casting spell sequence', self._run_spell_sequence)]

        for test in tests:
            print()
            print(color(3, f' {test[0]}...'))
            print(" " + "-" * 60)
            test[1]()
        print()

    def _run_spell_combiner(self) -> None:
        combined = spell_combiner(generate_spell_function(),
                                  generate_spell_function())
        target = random.choice(list(Targets)).value
        s1, s2 = combined(target, random.randint(5, 25))
        print(f' {color(7, "Spell 1"):<24}{s1}')
        print(f' {color(7, "Spell 2"):<24}{s2}')

    def _run_power_amplifier(self) -> None:
        spell = generate_spell_function()
        amplified_spell = power_amplifier(spell, random.randint(5, 25))
        target = random.choice(list(Targets)).value
        power = random.randint(5, 25)

        print(f' {color(7, "Base"):<24}{spell(target, power)}')
        print(f' {color(7, "Amplified"):<24}{amplified_spell(target, power)}')

    def _run_conditional_caster(self) -> None:
        cast_if = conditional_caster(valid_cast, generate_spell_function())
        target = random.choice(list(Targets)).value
        power = random.randint(5, 25)
        print(f' {color(6, 'All good'):<24}{cast_if(target, power)}')
        print(f' {color(5, 'Bad target'):<24}{cast_if('Banana', power)}')
        print(f' {color(5, 'Bad power'):<24}{cast_if(target, random.randint(-100, 0))}')

    def _run_spell_sequence(self) -> None:
        to_cast: list = []
        for _ in range(random.randint(5, 10)):
            spell = generate_spell_function()
            to_cast.append(spell)

        cast_all = spell_sequence(to_cast)

        target = random.choice(list(Targets)).value
        power = random.randint(5, 25)
        casted = cast_all(target, power)
        for spell in casted:
            print(f' {spell}')


# ----------------------------------------------------------------------------
#  Exercise 2: Memory Depths
# ----------------------------------------------------------------------------

class MemoryDepths():

    def __init__(self) -> None:
        pass

    def run_test(self) -> None:

        print()
        print(" " + "-" * 60)
        print(color(7, ' 🪄 Exercise 2: Memory Depths'))
        print(" " + "-" * 60)

        tests = [('Counting spells', self._run_mage_counter),
                  ('Accumulating power', self._run_spell_accumulator),
                  ('Enchanting items', self._run_enchantment_factory),
                  ('Memorizing spells', self._run_memory_vault)]

        for test in tests:
            print()
            print(color(3, f' {test[0]}...'))
            print(" " + "-" * 60)
            test[1]()
        print()

    def _run_mage_counter(self) -> None:
        mage_counters = []
        for idx in range(random.randint(2, 7)):
            mage_counters.append(mage_counter())

        for i in range(random.randint(2, 5)):
            for j in range(len(mage_counters)):
                n = j + 1
                print(f' {color(n, f"counter_{n}")} '
                      f'call {i + 1}: {mage_counters[j]()}')

    def _run_spell_accumulator(self) -> None:
        initial_power = random.randint(0, 1000)
        accumulator = spell_accumulator(initial_power)
        for _ in range(5):
            amount = random.randint(0, 1000)
            print(f' Base {initial_power}, add {amount}: {accumulator(amount)}')

    def _run_enchantment_factory(self) -> None:
        enchantment_type = random.choice(list(EnchantmentTypes)).value
        enchanter = enchantment_factory(enchantment_type)
        for _ in range(5):
            item_to_enchant = random.choice(list(Items)).value
            print(f' {enchanter(item_to_enchant)}')

    def _run_memory_vault(self) -> None:
        vault = memory_vault()
        store, recall = vault['store'], vault['recall']

        spells = random.sample([spell.value for spell in SpellNames], 2)
        known, unknown = spells[0], spells[1]
        power = random.randint(1, 100)

        store(known, power)
        print(f' Memorizing spell: {known} ({power})')
        print(f" Recalling {known}'s power: {recall(known)}")
        print(f" Recalling {unknown}'s power: {recall(unknown)}")


# ----------------------------------------------------------------------------
#  Exercise 3: Ancient Library
# ----------------------------------------------------------------------------

class AncientLibrary():

    def __init__(self) -> None:
        pass

    def run_test(self) -> None:

        print()
        print(" " + "-" * 60)
        print(color(7, ' 🪄 Exercise 3: Ancient Library'))
        print(" " + "-" * 60)

        tests = [('Transforming spells power', self._run_spell_reducer),
                  ('Partially enchanting', self._run_partial_enchanter),
                  ('Memoizing Fibonacci', self._run_memoized_fibonacci),
                  ('...', self._run_spell_dispatcher)]

        for test in tests:
            print()
            print(color(3, f' {test[0]}...'))
            print(" " + "-" * 60)
            test[1]()

        print()

    def _run_spell_reducer(self) -> None:
        operations: dict = {'Sum': 'add',
                            'Product': 'multiply',
                            'Max': 'max',
                            'Min': 'min'}

        spell_powers: list = []
        for _ in range(6):
            n = random.randint(-100, 100)
            spell_powers.append(n)

        for k, v in operations.items():
            print(f' {color(7, k):<22}{spell_reducer(spell_powers, v)}')

    def _run_partial_enchanter(self) -> None:
       pe = partial_enchanter(base_enchantment)
       target = random.choice(list(Items)).value
       for k, v in pe.items():
           print(' ' + v(target))

    def _run_memoized_fibonacci(self) -> None:
        fibonacci_tests = [0, 1]
        for _ in range(5):
            fibonacci_tests.append(random.randint(2, 100))
        fibonacci_tests = set(fibonacci_tests)
        for n in sorted(fibonacci_tests):
            print(f' {color(7, f'Fib({n})'):<21} {memoized_fibonacci(n)}')

    def _run_spell_dispatcher(self) -> None:
       dispatcher = spell_dispatcher()
       spells = generate_spell_dispatcher(10)
       for spell in spells:
           if isinstance(spell, int):
               print(f' {color(7, "Damage spell"):<26} {dispatcher(spell)}')
           elif isinstance(spell, str):
               print(f' {color(7, "Enchantment"):<26} {dispatcher(spell)}')
           elif isinstance(spell, list):
               print(f' {color(7, "Multi-cast"):<26} {dispatcher(spell)}')
           else:
               print(' ' + dispatcher(spell))


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
    print(color(7, f" {'n.':<5}{'Exercise':<20}{'Description'}"))
    print(" " + "-" * 60)
    print(f" {'0':<5}{'Lambda Sanctum':<20}"
          "Learn about lambda functions")
    print(f" {'1':<5}{'Higher Realm':<20}"
          "Learn about Callable data type")
    print(f" {'2':<5}{'Memory Depths':<20}"
          "Learn about lexical scoping")
    print(f" {'3':<5}{'Ancient Library':<20}"
          "Learn about functools")
    print(f" {'4':<5}{'Master’s Tower':<20}"
          "...")

    print()
    choice = input(color(3, ' 🪄 Enter your choice (0/1/2/3/4): '))

    if choice == "0":
        LambdaSanctum().run_test()
    elif choice == "1":
        HigherRealm().run_test()
    elif choice == "2":
        MemoryDepths().run_test()
    elif choice == "3":
        AncientLibrary().run_test()
    elif choice == "4":
        pass
    else:
        print(color(5, ' ERROR! Invalid choice! Please enter 0, 1, 2, 3, or 4'))


if __name__ == "__main__":
    func_mage()
