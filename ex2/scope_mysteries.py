"""
Exercise 2: Memory Depths
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

def mage_counter() -> Callable:
    pass


def spell_accumulator(initial_power: int) -> Callable:
    pass


def enchantment_factory(enchantment_type: str) -> Callable:
    pass


def memory_vault() -> dict[str, Callable]:
    pass


# ----------------------------------------------------------------------------
#  Testing...
# ----------------------------------------------------------------------------

def main() -> None:

    initial_powers = [74, 62, 50]
    power_additions = [5, 14, 5, 8, 12]
    enchantment_types = ['Flaming', 'Shocking', 'Frozen']
    items_to_enchant = ['Cloak', 'Armor', 'Wand', 'Amulet']

    # --- Testing mage_counter()

    try:
        print()
        print(color(3, ' Testing Mage Counter...'))

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing spell_accumulator()

    try:
        print()
        print(color(3, ' Testing Spell Accumulator...'))

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing enchantment_factory()

    try:
        print()
        print(color(3, ' Testing Enchantment Factory...'))

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing memory_vault()

    try:
        print()
        print(color(3, ' Testing Memory Vault...'))

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    print()


if __name__ == "__main__":
    main()
