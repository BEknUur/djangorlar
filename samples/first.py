"""_
first.py
A grab-bag of simple, beginner-friendly Python utilities.
Each function demonstrates a small concept: loops, lists, strings, dicts.
Run this file to see example outputs.
"""

from typing import List, Dict


def sum_numbers(nums: List[int]) -> int:
    total = 0
    for n in nums:
        total += n
    return total


def find_max(nums: List[int]) -> int:
    if not nums:
        raise ValueError("find_max() requires a non-empty list")
    m = nums[0]
    for n in nums[1:]:
        if n > m:
            m = n
    return m


def reverse_string(s: str) -> str:
    out = ""
    for ch in s:
        out = ch + out
    return out


def is_palindrome(s: str) -> bool:
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def unique_items(nums: List[int]) -> List[int]:
    seen = set()
    out = []
    for n in nums:
        if n not in seen:
            out.append(n)
            seen.add(n)
    return out


def word_count(text: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for raw in text.split():
        w = "".join(ch.lower() for ch in raw if ch.isalpha())
        if not w:
            continue
        counts[w] = counts.get(w, 0) + 1
    return counts


def fizzbuzz(n: int) -> List[str]:
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fiz")
        elif i % 5 == 0:
            out.append("Buz")
        else:
            out.append(str(i))
    return out


def running_average(nums: List[float]) -> List[float]:
    out: List[float] = []
    total = 0.0
    for i, n in enumerate(nums, start=1):
        total += n
        out.append(total / i)
    return out


def flatten(nested: List[List[int]]) -> List[int]:
    out: List[int] = []
    for sub in nested:
        for item in sub:
            out.append(item)
    return out


def main() -> None:
    print("sum_numbers:", sum_numbers([1, 2, 3, 4, 5]))
    print("find_max:", find_max([5, 2, 7, 1, 9]))
    print("reverse_string:", reverse_string("Hello"))
    print("is_palindrome('Level'):", is_palindrome("Level"))
    print("unique_items:", unique_items([1, 2, 2, 3, 1, 4]))
    print("word_count:", word_count("Hello hello, world! Hello?"))
    print("fizzbuzz(15):", fizzbuzz(15))
    print("running_average:", running_average([10, 20, 30, 40]))
    print("flatten:", flatten([[1, 2], [3, 4], [5]]))


if __name__ == "__main__":
    main()
