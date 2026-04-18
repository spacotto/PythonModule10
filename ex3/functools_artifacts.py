"""
Exercise 3: Ancient Library
"""


# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

from collections.abc import Callable
import functools
import operator
from typing import Any


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

def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Reduce spell powers:
    • Use functools.reduce to combine all spell powers
    • Support operations: "add", "multiply", "max", "min"
    • Use operator module functions (add, mul, etc.)
    • Return the final reduced value
    • If spells is empty, return 0
    • If operation is unknown, properly handle the error
    """
    if not spells:
        return 0

    ops = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """
    Create partial applications:
    • Take a base enchantment function with signature
      (power: int, element: str, target: str) -> str
    • Use functools.partial to create 3 specialized versions
    • Each version pre-filling power=50 and the element
    """
    return {
        'flaming': functools.partial(base_enchantment, 50, 'Flaming'),
        'frozen': functools.partial(base_enchantment, 50, 'Frozen'),
        'shocking': functools.partial(base_enchantment, 50, 'Shocking')
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    Cached fibonacci:
    • Use functools.lru_cache decorator for memoization
    • Implement fibonacci sequence calculation
    • Function should return the nth Fibonacci number
    • The cache should improve performance for repeated calls
    • Return the nth fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """
    Create single dispatch system:
    • Use decorator functools.singledispatch to create a spell system
    • The base function receives Any and handles unknown spell type
    • Handle different types: int (damage spell), str (enchantment), list (multi-cast)
    • Return the dispatcher function
    • Each type should have appropriate spell behavior
    """
    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"{spell} damage"

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return spell

    @dispatcher.register(list)
    def _(spell: list) -> str:
        return f"{len(spell)} spells"

    return dispatcher


# ----------------------------------------------------------------------------
#  Testing...
# ----------------------------------------------------------------------------

def main() -> None:

    # --- Testing spell_reducer()

    spell_powers = [50, 44, 27, 17, 34, 16]
    operations = {'Sum': 'add',
                  'Product': 'multiply',
                  'Max': 'max',
                  'Min': 'min'}

    try:
        print()
        print(color(3, ' Testing spell reducer...'))
        for k, v in operations.items():
            print(f' {color(7, k):<22}{spell_reducer(spell_powers, v)}')

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing partial_enchanter()

    try:
        print()
        print(color(3, ' Testing partial enchanter...'))

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing memoized_fibonacci()

    fibonacci_tests = [16, 19, 15]

    try:
        print()
        print(color(3, ' Testing memoized fibonacci...'))

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing spell_dispatcher()

    try:
        print()
        print(color(3, ' Testing spell dispatcher...'))

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    print()


if __name__ == "__main__":
    main()
