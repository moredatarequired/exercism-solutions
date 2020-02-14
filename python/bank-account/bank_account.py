from functools import wraps
from multiprocessing import Lock


def locked(f):
    @wraps(f)
    def wrapper(self, *args, **kwds):
        with self._BankAccount__account_lock:
            return f(self, *args, **kwds)

    return wrapper


def open_must_be(state):
    def wrapper(f):
        error = f"Cannot {f.__name__} {'a closed' if state else 'an open'} account"

        @wraps(f)
        def wrapped(self, *args, **kwds):
            if self._BankAccount__open == state:
                return f(self, *args, **kwds)
            raise ValueError(error)

        return wrapped

    return wrapper


class BankAccount:
    def __init__(self, is_open=False, balance=0):
        self.__open = is_open
        self.__balance = balance
        self.__account_lock = Lock()

    def __repr__(self):
        return f"{self.__class__.__name__}(is_open={self.__open}, balance={self.__balance})"

    @locked
    @open_must_be(True)
    def get_balance(self):
        return self.__balance

    @locked
    @open_must_be(False)
    def open(self):
        self.__open = True

    @locked
    @open_must_be(True)
    def close(self):
        self.__open = False
        self.__balance = 0

    @locked
    @open_must_be(True)
    def deposit(self, amount):
        if amount < 0:
            raise ValueError(f"deposit called with ${amount} (must be non-negative)")
        self.__balance += amount

    @locked
    @open_must_be(True)
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError(f"withdraw called with ${amount} (must be non-negative)")
        if self.__balance < amount:
            raise ValueError(f"Insufficient balance: ${self.__balance} < ${amount}")
        self.__balance -= amount
