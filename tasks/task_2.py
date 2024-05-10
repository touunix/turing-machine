"""
Describe an MT that calculates the number of 1's in its input word.
"""
from utilities.generator import Generator


class Program:
    @staticmethod
    def count_ones(binary_string: str) -> int:
        one_count: int = 0
        for bit in binary_string:
            if bit == "1":
                one_count += 1
        return one_count


if __name__ == "__main__":
    binary_length: int = Generator.generate_random_length()
    binary_number: str = Generator.generate_random_binary(binary_length)
    binary_result: int = Program.count_ones(binary_number)

    print(60 * "-")
    print(f"Generated random binary number: {binary_number}")
    print(60 * "-")
    print(f"Number of occurrences of ones: {binary_result}")
    print(60 * "-")
