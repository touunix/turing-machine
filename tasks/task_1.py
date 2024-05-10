"""
Describe an MT that adds 1 to a binary number stored on tape.
"""
from utilities.generator import Generator


class Program:
    @staticmethod
    def add_one_to_binary(binary_string: str) -> str:
        binary_list: list = list(binary_string)
        carry: int = 1

        # iterate from the end of the binary number
        for index in range(len(binary_list) - 1, -1, -1):  # start, stop, step
            if binary_list[index] == "0":  # if the current bit is 0, add 1 and do not carry
                binary_list[index]: str = "1"
                carry: int = 0
                break  # added 1
            else:  # if the current bit is 1, change it to 0 and carry 1
                binary_list[index]: str = "0"

        # if we still have a carry, add 1 at the beginning
        if carry:
            binary_list.insert(0, carry)
        return "".join(binary_list)


if __name__ == "__main__":
    binary_length: int = Generator.generate_random_length()
    binary_number: str = Generator.generate_random_binary(binary_length)
    binary_result: str = Program.add_one_to_binary(binary_number)

    print(60 * "-")
    print(f"Generated random binary number: {binary_number}")
    print(60 * "-")
    print(f"Binary number after addition of 1: {binary_result}")
    print(60 * "-")
