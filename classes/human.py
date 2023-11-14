class Human:
    # 1. Humans initialize with a `first_name` and `last_name`.

    # 2. Humans initialize with an `_age` of 0. This will be a property (`age`) later.

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0

    # 3. Give humans a `__repr__` that adequately shows their characteristics. You decide what this looks like.

    def __repr__(self):
        return f"Human(first name={self.first_name}, last_name={self.last_name}, age={self._age})"

    # 4. Give humans a method `say_full_name` which returns their concatenated `first_name` and `last_name`.

    def say_full_name(self):
        return f"{self.first_name} {self.last_name}"

    # 5. Give humans a method `happy_birthday` which increments that human's age by 1.

    def happy_birthday(self):
        self._age += 1
        return self._age

    # 6. Give humans a property `age`. When someone attempts to set a human's `age` directly it instead doesn't change and returns the string `"Quit lying about your age!"`.

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        raise TypeError("Quit lying about your age!")