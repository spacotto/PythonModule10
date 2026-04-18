"""
Exercise 3: Ancient Library
"""


# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

from collections.abc import Callable


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
    pass


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """
    Create partial applications:
    • Take a base enchantment function with signature
      (power: int, element: str, target: str) -> str
    • Use functools.partial to create 3 specialized versions
    • Each version pre-filling power=50 and the element
    """
    pass


def memoized_fibonacci(n: int) -> int:
    """
    Cached fibonacci:
    • Use functools.lru_cache decorator for memoization
    • Implement fibonacci sequence calculation
    • Function should return the nth Fibonacci number
    • The cache should improve performance for repeated calls
    • Return the nth fibonacci number
    """
    pass


def spell_dispatcher() -> Callable[[Any], str]:
    """
    Create single dispatch system:
    • Use decorator functools.singledispatch to create a spell system
    • The base function receives Any and handles unknown spell type
    • Handle different types: int (damage spell), str (enchantment), list (multi-cast)
    • Return the dispatcher function
    • Each type should have appropriate spell behavior
    """
    pass


# ----------------------------------------------------------------------------
#  Testing...
# ----------------------------------------------------------------------------

def main() -> None:

    spell_powers = [50, 44, 27, 17, 34, 16]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [16, 19, 15]

    # --- Testing ()

    try:
        print()
        print(color(3, ' Testing ...'))

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing ()

    try:
        print()
        print(color(3, ' Testing ...'))

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing ()

    try:
        print()
        print(color(3, ' Testing ...'))

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing ()

    try:
        print()
        print(color(3, ' Testing ...'))

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    print()


if __name__ == "__main__":
    main()
