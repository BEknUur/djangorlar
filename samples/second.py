"""
second_bank.py
A tiny in-memory "bank" model for practicing classes and methods.
Demonstrates deposits, withdrawals, transfers, and a transaction log.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class Transaction:
    kind: str
    amount: float
    note: str = ""

    def __str__(self) -> str:
        return f"[{self.kind}] amount={self.amount:.2f} note={self.note or '-'}  "



@dataclass
class Account:
    owner: str
    balance: float = 0.0
    history: List[Transaction] = field(default_factory=list)

    def deposit(self, amount: float, note: str = "") -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self.history.append(Transaction("DEPOSIT", amount, note))

    def withdraw(self, amount: float, note: str = "") -> None:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.history.append(Transaction("WITHDRAW", amount, note))

    def transfer_to(self, other: "Account", amount: float) -> None:
        self.withdraw(amount, note=f"to {other.owner}")
        other.deposit(amount, note=f"from {self.owner}")

    def statement(self) -> str:
        lines = [f"=== Statement for {self.owner} ===", f"Balance: {self.balance:.2f}", "History:"]
        lines += [f"  - {t}" for t in self.history]
        return "\n".join(lines)


def demo() -> None:
    alice = Account("Alice")
    bob = Account("Bob", balance=50.0)

    alice.deposit(100.0, "initial")
    alice.withdraw(30.0, "groceries")
    alice.transfer_to(bob, 20.0)
    bob.deposit(15.0, "gift")
    try:
        bob.withdraw(1000.0, "oops")
    except ValueError as e:
        print("Expected error:", e)

    print(alice.statement())
    print()
    print(bob.statement())


if __name__ == "__main__":
    demo()
