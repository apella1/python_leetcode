def roman_to_integer(text: str) -> int:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    for letter in range(len(text)):
        if letter + 1 < len(text) and roman[text[letter]] < roman[text[letter + 1]]:
            result -= roman[text[letter]]
        else:
            result += roman[text[letter]]

    return result


print(roman_to_integer("IX"))
