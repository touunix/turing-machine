"""
Write a program that concatenates two binary numbers separated by a
blank. The first number is to be appended to the end of the second.
For example, if the null character is ?, then the
input 110011?101 should result in 101110011.
"""
from utilities.generator import Generator


class Program:
    @staticmethod
    def concatenate_binary_numbers(binary_string: str) -> str:
        parts: list = binary_string.split("?")
        first_number: str = parts[0]
        second_number: str = parts[1]
        return second_number + first_number


if __name__ == "__main__":
    first_binary_length: int = Generator.generate_random_length()
    first_binary_number: str = Generator.generate_random_binary(first_binary_length)
    second_binary_length: int = Generator.generate_random_length()
    second_binary_number: str = Generator.generate_random_binary(second_binary_length)

    binary_number: str = f"{first_binary_number}?{second_binary_number}"
    binary_result: str = Program.concatenate_binary_numbers(binary_number)

    print(60 * "-")
    print(f"Generated random first binary number: {first_binary_number}")
    print(f"Generated random second binary number: {second_binary_number}")
    print(60 * "-")
    print(f"Generated random binary number: {binary_number}")
    print(60 * "-")
    print(f"Concatenated binary numbers: {binary_result}")
    print(60 * "-")
