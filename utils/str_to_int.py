def str_to_int(value: str) -> int:
    result = 0
    pos = 10                         # makes position for next digit in the resulting number
    for ch in value:
        if (ch.isdigit()):
            result *= pos
            result += int(ch)
        else:
            return 0
    return result


if __name__ == '__main__':
    test = input("Enter an integer value ")
    print(str_to_int(test))
