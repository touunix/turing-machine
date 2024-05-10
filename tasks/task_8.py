"""
Write a program that doubles each bit of an input binary number.
For example, from the number 101 we should get 110011.
"""
from utilities.generator import Generator


class Program:
    @staticmethod
    def double_bits(binary_string: str) -> str:
        doubled_number: str = ""
        for bit in binary_string:
            doubled_number += bit * 2
        return doubled_number


if __name__ == "__main__":
    binary_length: int = Generator.generate_random_length()
    binary_number: str = Generator.generate_random_binary(binary_length)
    binary_result: str = Program.double_bits(binary_number)

    print(60 * "-")
    print(f"Generated random binary number: {binary_number}")
    print(60 * "-")
    print(f"Binary number after bit doubling: {binary_result}")
    print(60 * "-")
