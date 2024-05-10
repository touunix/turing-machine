"""
Write a program that zeros the middle bits of a binary number. At
For example, the number 101111 should go to 100001.
"""
from utilities.generator import Generator


class Program:
    @staticmethod
    def zero_middle_bits(binary_string: str) -> str:
        if len(binary_string) < 3:  # at least 3 bits are required for zero
            return binary_string

        middle_bits: str = binary_string[1:-1]
        zeroed_middle_bits: str = "0" * len(middle_bits)
        return binary_string[0] + zeroed_middle_bits + binary_string[-1]


if __name__ == "__main__":
    binary_length: int = Generator.generate_random_length()
    binary_number: str = Generator.generate_random_binary(binary_length)
    binary_result: str = Program.zero_middle_bits(binary_number)

    print(60 * "-")
    print(f"Generated random binary number: {binary_number}")
    print(60 * "-")
    print(f"Binary number after resetting the middle bits: {binary_result}")
    print(60 * "-")
