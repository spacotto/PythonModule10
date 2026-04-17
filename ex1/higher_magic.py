"""
Exercise 1: Higher Realm
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

from collections.abc import Callable


# ----------------------------------------------------------------------------
#  Functions
# ----------------------------------------------------------------------------

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """
    Combine two spells:
    • Return a new function that calls both spells with the same arguments
    • The combined spell should return a tuple of both results
    • Example: combined = spell_combiner(fireball, heal)
    """
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """
    Amplify spell power:
    • Returns a function with the same signature as the original spell
    • Returns a new spell where the power is multiplied before casting.
    • Example: mega_fireball = power_amplifier(fireball, 3)
    """
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified(base_spell, multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """
    Cast spell conditionally:
    • Returns a new spell that only casts if a condition is True.
    • If condition fails, return "Spell fizzled"
    • Both condition and spell receive the same arguments
    """
    return cast_if


def spell_sequence(spells: list[Callable]) -> Callable:
    """
    Create spell sequence:
    • Return a function that casts all spells in order
    • Each spell receives the same arguments
    • Returns a list of all spell results
    """
    return cast_all


# ----------------------------------------------------------------------------
#  Callables
# ----------------------------------------------------------------------------

def fireball(target: str, power: int) -> str:
    return f'Fireball deals {power} damage(s) to {target}'


def heal(target: str, power: int) -> str:
    return f'Heal restores {target} for {power} HP'


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} defense"


def lightning(target: str, power: int) -> str:
    return f'Lightning deals {power} damage(s) to {target}'


def freeze(target: str, power: int) -> str:
    return f'Freeze deals {power} damage(s) to {target}'


def earthquake(target: str, power: int) -> str:
    return f'Earthquake deals {power} damage(s) to {target}'


def tornado(target: str, power: int) -> str:
    return f'Tornado deals {power} damage(s) to {target}'


def tsunami(target: str, power: int) -> str:
    return f'Tsunami deals {power} damage(s) to {target}'


def flash(target: str, power: int) -> str:
    return f'Flash deals {power} damage(s) to {target}'


def darkness(target: str, power: int) -> str:
    return f'Darkness deals {power} damage(s) to {target}'


def meteor(target: str, power: int) -> str:
    return f'Meteor deals {power} damage(s) to {target}'


def blizzard(target: str, power: int) -> str:
    return f'Blizzard deals {power} damage(s) to {target}'


# ----------------------------------------------------------------------------
#  Testing...
# ----------------------------------------------------------------------------

def main() -> None:

    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    test_values = [16, 13, 7]

    # --- Testing spell_combiner()

    try:
        print()
        print(color(3, ' Testing spell combiner...'))
        combined = spell_combiner(fireball, heal)
        c = combined(test_targets[0], test_values[0])
        print(f' Combined spell result: {c[0]}, {c[1]}')

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing power_amplifier()

    try:
        print()
        print(color(3, ' Testing power amplifier...'))
        print(power_amplifier(10, 3))
        mega_fireball = power_amplifier(fireball, 3)
        print('Original: 10, Amplified: 30')

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing conditional_caster()

    try:
        print()
        print(color(3, ' Testing conditional caster...'))
        print(conditional_caster())

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing spell_sequence()

    try:
        print()
        print(color(3, ' Testing spell sequence...'))
        print(spell_sequence())

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    print()


if __name__ == "__main__":
    main()
