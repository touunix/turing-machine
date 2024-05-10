"""
Write a program that replaces in any text built
of the letters A, B, C and D by replacing all the letters A with C. For example, from the
BACA text is to form BCCC.
"""
from utilities.generator import Generator


class Program:
    @staticmethod
    def replace_a_with_c(text: str) -> str:
        replaced_text: str = ""
        for character in text:
            if character == "A":
                replaced_text += "C"
            else:
                replaced_text += character
        return replaced_text


if __name__ == "__main__":
    input_length: int = Generator.generate_random_length()
    input_text: str = Generator.generate_random_text_abcd(input_length)
    result_text: str = Program.replace_a_with_c(input_text)

    print(60 * "-")
    print(f"Generated random input text: {input_text}")
    print(60 * "-")
    print(f"Text after the conversion of A to C: {result_text}")
    print(60 * "-")
