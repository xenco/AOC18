from functools import lru_cache
import sys
sys.setrecursionlimit(10000)

@lru_cache(maxsize=None)
def reaction(polymer):
    for i in range(0, len(polymer) - 1):
        if polymer[i].casefold() == polymer[i+1].casefold():
            if (polymer[i].islower() and polymer[i+1].isupper()) or (polymer[i].isupper() and polymer[i+1].islower()):
                return reaction(polymer.replace(polymer[i] + polymer[i + 1], ""))
    return polymer

def replaceUnit(polymer, unit):
    return polymer.replace(unit.lower(), "").replace(unit.upper(), "")

def main():
    with open("input") as f:
        str_polymer = f.read()
    f.close()

    min_len = None
    for unit in [chr(i) for i in range(97, 123)]:
        str_polymer_cleaned = replaceUnit(str_polymer, unit)
        polymer = reaction(str_polymer_cleaned)

        min_len = len(polymer) if min_len is None else (len(polymer) if len(polymer) < min_len else min_len)

    print("Result: ", min_len)


if __name__ == '__main__':
    main()