import random


class Generator:
    @staticmethod
    def generate_random_length() -> int:
        return random.randint(a=0, b=25)

    @staticmethod
    def generate_random_binary(length: int) -> str:
        random_binary: list = [random.choice(["0", "1"]) for _ in range(length)]
        return "".join(random_binary)

    @staticmethod
    def generate_random_text_abcd(length: int) -> str:
        random_text: list = [random.choice(["A", "B", "C", "D"]) for _ in range(length)]
        return "".join(random_text)
