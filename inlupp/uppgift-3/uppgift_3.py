def max_in_list(numbers: list[int]) -> int:
    """

    """

    largest = numbers[0]

    for num in numbers[1:]:
        if num > largest:
            largest = num

    return largest

print(max_in_list([1, 2, 3]))