def find_max(numbers):
    if not numbers:
        return None, None
    max_value = numbers[0]
    max_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
            max_index = i
def find_max_while(numbers):
    if not numbers:
        return None, None
    max_value = numbers[0]
    max_index = 0
    i = 1
    while i < len(numbers):
        if numbers[i] > max_value:
            max_value = numbers[i]
            max_index = i
        i += 1
    return max_value, max_index