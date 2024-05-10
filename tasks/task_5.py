"""
Write a program that swaps the beginning and end bits of a
binary number. For example, the number 11010 should go into 01011.
"""
from utilities.generator import Generator


class Program:
    @staticmethod
    def swap_first_and_last_bit(binary_string: str) -> str:
        if len(binary_string) < 2:  # at least 2 bits are required for swap
            return binary_string
        return binary_string[-1] + binary_string[1:-1] + binary_string[0]


if __name__ == "__main__":
    binary_length: int = Generator.generate_random_length()
    binary_number: str = Generator.generate_random_binary(binary_length)
    binary_result: str = Program.swap_first_and_last_bit(binary_number)

    print(60 * "-")
    print(f"Generated random binary number: {binary_number}")
    print(60 * "-")
    print(f"Binary number after swap the first and last bits: {binary_result}")
    print(60 * "-")
