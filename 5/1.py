from functools import lru_cache
import sys

sys.setrecursionlimit(10000)


@lru_cache(maxsize=None)
def reaction(polymer):
    for i in range(0, len(polymer) - 1):
        if polymer[i].casefold() == polymer[i + 1].casefold():
            if (polymer[i].islower() and polymer[i + 1].isupper()) or (
                    polymer[i].isupper() and polymer[i + 1].islower()):
                return reaction(polymer.replace(polymer[i] + polymer[i + 1], ""))
    return polymer


with open("input") as f:
    str_polymer = f.read()
f.close()

polymer = reaction(str_polymer)
print("Result: ", len(polymer))
