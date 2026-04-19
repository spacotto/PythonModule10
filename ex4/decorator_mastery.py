"""
Exercise 4: Master’s TowerI
"""


# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

from collections.abc import Callable
import functools
import time


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
#  Functions
# ----------------------------------------------------------------------------

def spell_timer(func: Callable) -> Callable:
    """
    Time execution decorator:
    • Create a decorator that measures function execution time
    • Print "Casting <function_name>..." before execution
    • Print "Spell completed in X.XXX seconds" after execution (3 dec places)
    • Use functools.wraps to preserve original function metadata
    • Return the original function’s result
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f" Casting {func.__name__}...")
        start_time = time.time()
        time.sleep(0.101)
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f" Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """
    Parameterized validation decorator:
    • Create a decorator factory that validates power levels
    • Applied on a standalone function whose first argument is power.
    • If power is valid (>= min_power), execute the function normally
    • If invalid, return "Insufficient power for this spell"
    • Use functools.wraps properly
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get('power')
            if power is None:
                power = next((arg for arg in reversed(args)
                              if isinstance(arg, int)), 0)

            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """
    Retry decorator:
    • Create a decorator that retries failed spells
    • If function raises an exception, retry up to max_attempts times
    • Print "Spell failed, retrying... (attempt n/max_attempts)"
    • If all attempts fail, return
      "Spell casting failed after <max_attempts> attempts"
    • If one attempt succeeds, return its result normally
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f' Spell failed, retrying... '
                          f'(attempt {attempt}/{max_attempts})')
            return f' Spell casting failed after {max_attempts} attempts'
        return wrapper
    return decorator


class MageGuild():

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        Static method that checks if name is valid:
        • At least 3 char and
        • Contains only letters/spaces
        """
        if len(name) < 3:
            return False
        if not all(c.isalpha() or c.isspace() for c in name):
            return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """
        Instance method
        • Should use the power_validator decorator with min_power=10
        • When power is valid, return:
          "Successfully cast <spell_name> with <power> power"
        • Otherwise return:
          "Insufficient power for this spell"
        """
        return f"Successfully cast {spell_name} with {power} power"


# ----------------------------------------------------------------------------
#  Helpers
# ----------------------------------------------------------------------------

def fireball() -> str:
    return 'Fireball cast!'


@retry_spell(max_attempts=3)
def spell(power: int) -> str:
    if power < 1:
        raise ValueError
    return ' Waaaaaaagh spelled !'


# ----------------------------------------------------------------------------
#  Testing...
# ----------------------------------------------------------------------------

def main() -> None:

    # --- Testing spell_timer()

    try:
        print()
        print(color(3, ' Testing spell time...'))
        wrapper = spell_timer(fireball)
        print(' Result: ' + wrapper())

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing retry_spell()

    try:
        print()
        print(color(3, ' Testing retrying spell...'))

        print(spell(-42))
        print(spell(42))

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing MageGuild()

    mage_names_a = ['Ash and Zara', ':)']
#    mage_names_b = ['Ash', 'Zara', 'Jordan', 'Luna', 'Alex', 'Morgan',
#                    'Jo', 'A', 'Alex123', 'Test@Name']

    spells_a = {'Lightning': 15, 'Fireball': 3}
#    spells_b = {'Lightning': 15, 'Meteor': 9, 'Fireball': 3, 'Freeze': 10}

    try:
        print()
        print(color(3, ' Testing MageGuild...'))
        mg = MageGuild()

        print()
        for name in mage_names_a:
            print(f' {name:<16}' + str(mg.validate_mage_name(name)))

        print()
        for k, v in spells_a.items():
            print(' ' + mg.cast_spell(k, v))

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    print()


if __name__ == "__main__":
    main()
