"""
Write a program that moves the first letter of a word
made up of the letters A, B, C and D from the beginning to the end. For example, from
DAB text is to produce ABD.
"""
from utilities.generator import Generator


class Program:
    @staticmethod
    def move_first_letter_to_end(word: str) -> str:
        if len(word) < 2:
            return word
        first_letter: str = word[0]
        rest_of_word: str = word[1:]
        return rest_of_word + first_letter


if __name__ == "__main__":
    input_length: int = Generator.generate_random_length()
    input_text: str = Generator.generate_random_text_abcd(input_length)
    result_text: str = Program.move_first_letter_to_end(input_text)

    print(60 * "-")
    print(f"Generated random input text: {input_text}")
    print(60 * "-")
    print(f"After moving the first letter to the end: {result_text}")
    print(60 * "-")
