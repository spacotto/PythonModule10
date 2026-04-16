"""
Exercise 0: Lambda Sanctum
"""


# ----------------------------------------------------------------------------
#  Visual helpers
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

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    Sort magical artifacts:
    - Use sorted() with a lambda to sort by ’power’ level (descending)
    - Each artifact is a dict: {’name’: str, ’power’: int, ’type’: str}
    - Return the sorted list
    """
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """
    Filter mages by power:
    - Use filter() with a lambda to find mages with power >= min_power
    - Each mage is a dict: {’name’: str, ’power’: int, ’element’: str}
    - Return a list of filtered mages
    """
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Transform spell names:
    - Use map() with a lambda to add "* " prefix and " *" suffix
    - Input: list of spell names (strings)
    - Return a list of transformed spell names
    """
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """
    Calculate statistics:
    - Use lambdas with max(), min() to find:
      - Most powerful mage’s power level
      - Least powerful mage’s power level
      - Average power level (rounded to 2 decimals)
    - Return dict: {’max_power’: int, ’min_power’: int, ’avg_power’: float}
    """
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    powers = list(map(lambda m: m['power'], mages))

    return {
        'max_power': max(powers, key=lambda p: p),
        'min_power': min(powers, key=lambda p: p),
        'avg_power': round(sum(powers) / len(mages), 2)
    }


def main() -> None:

    artifacts = [{'name': 'Crystal Orb',
                  'power': 85,
                  'type': 'focus'},
                 {'name': 'Fire Staff',
                  'power': 92,
                  'type': 'relic'},]
    try:
        print()
        print(color(3, ' Testing artifact sorter...'))
        x = artifact_sorter(artifacts)
        print(f' {x[0]['name']} ({x[0]['power']} power) comes before'
              f' {x[1]['name']} ({x[1]['power']} power)')

    except Exception as e:
        print()
        print(color(5, f'\n ERROR! {e}\n'))

    spells = ['fireball', 'heal', 'shield']

    try:
        print()
        print(color(3, ' Testing spell transformer...'))
        y = spell_transformer(spells)
        print(f' {y[0]}{y[1]}{y[2]}')

    except Exception as e:
        print()
        print(color(5, f'\n ERROR! {e}\n'))

    print()


if __name__ == "__main__":
    main()
