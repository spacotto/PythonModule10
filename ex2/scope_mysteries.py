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
    """
    Create a counting closure:
    • Return a function that counts how many times it’s been called
    • Each call should return the current count (starting from 1)
    • The counter should persist between calls
    • Creating two separate counters must yield independent state.
    • Use closure to maintain state without global variables
    """
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """
    Create power accumulator:
    • Return a function that accumulates power over time
    • Each call adds the given amount to the total power
    • Return the new total power after each addition
    • Start with initial_power as the base
    """
    def accumulator(amount: int) -> int:
        nonlocal initial_power
        initial_power += amount
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    """
    Create enchantment functions:
    • Return a function that applies the specified enchantment
    • The returned fn takes an item name and returns enchanted description
    • Format: "enchantment_type item_name" (e.g., "Flaming Sword")
    • Each factory creates functions with different enchantment types
    """
    def enchanter(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchanter


def memory_vault() -> dict[str, Callable]:
    """
    Create a memory management system:
    • Return a dict with ’store’ and ’recall’ functions
    • ’store’ fn: takes (k, v) and stores the memory
    • ’recall’ fn: takes (k) and returns stored v or "Memory not found"
    • Use closure to maintain private memory storage
    """
    pass


# ----------------------------------------------------------------------------
#  Testing...
# ----------------------------------------------------------------------------

def main() -> None:

    # --- Testing mage_counter()

    try:
        print()
        print(color(3, ' Testing Mage Counter...'))

        counter_a = mage_counter()
        for idx in range(2):
            print(f' counter_a call {idx + 1}: {counter_a()}')

        counter_b = mage_counter()
        for idx in range(1):
            print(f' counter_b call {idx + 1}: {counter_b()}')

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing spell_accumulator()

    initial_powers = [100, 150, 200, 250, 300]
    power_additions = [20, 30]

    try:
        print()
        print(color(3, ' Testing Spell Accumulator...'))
        ip = initial_powers[0]
        accumulator = spell_accumulator(ip)
        for amount in power_additions:
            print(f' Base {ip}, add {amount}: {accumulator(amount)}')

    except Exception as e:
        print(color(5, f'\n ERROR! {e}\n'))

    # --- Testing enchantment_factory()

    enchantment_types = ['Flaming', 'Frozen', 'Shocking']
    items_to_enchant = ['Sword', 'Shield', 'Cloak', 'Armor', 'Wand']

    try:
        print()
        print(color(3, ' Testing Enchantment Factory...'))

        enchanter_a = enchantment_factory(enchantment_types[0])
        print(f' {enchanter_a(items_to_enchant[0])}')

        enchanter_b = enchantment_factory(enchantment_types[1])
        print(f' {enchanter_b(items_to_enchant[1])}')

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
