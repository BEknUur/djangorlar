"""
third.py
A minimal "library" with Book and Library classes.
Shows: add/remove/search, list operations, and JSON export.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import List, Optional
import json


@dataclass
class Book:
    title: str
    author: str
    year: int
    tags: List[str]

    def matches(self, keyword: str) -> bool:
        k = keyword.lower()
        hay = " ".join([self.title, self.author, *self.tags]).lower()
        return k in hay


class Library:
    def __init__(self) -> None:
        self._books: List[Book] = []

    def add(self, book: Book) -> None:
        self._books.append(book)

    def remove(self, title: str) -> bool:
        for i, b in enumerate(self._books):
            if b.title == title:
                del self._books[i]
                return True
        return False

    def search(self, keyword: str) -> List[Book]:
        return [b for b in self._books if b.matches(keyword)]

    def get(self, title: str) -> Optional[Book]:
        for b in self._books:
            if b.title == title:
                return b
        return None

    def to_json(self) -> str:
        data = [asdict(b) for b in self._books]
        payload={"count":len(data), "items":data}
        return json.dumps(payload, ensure_ascii=False, indent=2)

    def __len__(self) -> int:
        return len(self._books)


def seed_sample(lib: Library) -> None:
    lib.add(Book("The Pragmatic Programmer", "Andrew Hunt", 1999, ["software", "craft"]))
    lib.add(Book("Clean Code", "Robert C. Martin", 2008, ["software", "best-practices"]))
    lib.add(Book("Deep Work", "Cal Newport", 2016, ["focus", "productivity"]))
    lib.add(Book("Atomic Habits", "James Clear", 2018, ["habits", "self-help"]))
    lib.add(Book("The Hobbit", "J. R. R. Tolkien", 1937, ["fantasy", "adventure"]))


def demo() -> None:
    lib = Library()
    seed_sample(lib)
    print("Books in library:", len(lib))
    print("Search 'software':", [b.title for b in lib.search("software")])
    print("Search 'hobbit':", [b.title for b in lib.search("hobbit")])
    removed = lib.remove("Deep Work")
    print("Removed 'Deep Work':", removed)
    print("JSON Export:\n", lib.to_json())


if __name__ == "__main__":
    demo()
