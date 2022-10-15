def max_digit(number: int) -> int:
    number_str = str(number)
    if len(number_str) == 1:
        return number
    else:
        number_list = []
        for el in number_str:
            number_list.append(int(el))
        return max(number_list)


if __name__ == '__main__':
    print("Example:")
    print(max_digit(5648))