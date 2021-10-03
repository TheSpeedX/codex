from time import time


def is_palindrome(number):
    """returns True for a palindrome, False otherwise."""
    to_str = str(number)
    return to_str == to_str[::-1]


def add_reverses(number, count):
    """makes a list of reverses for a number at a maximum iteration of count, breaks if palindrome found below count."""
    reverses = [number]
    for _ in range(count):
        last_number = reverses[-1]
        new_number = int(str(reverses[-1])[::-1])
        if is_palindrome(last_number + new_number):
            reverses.append(last_number + new_number)
            return reverses
        else:
            reverses.append(last_number + new_number)
    return reverses


def count_lychrel_range(number_range, count):
    """returns Lychrel numbers within number_range, assumes count is the maximum iterations for a number."""
    total = 0
    numbers_reverses = {}
    for number in range(number_range):
        numbers_reverses[number] = add_reverses(number, count)
    for number, rev_sequence in numbers_reverses.items():
        if len(rev_sequence) >= count:
            total += 1
    return total


if __name__ == '__main__':
    start_time = time()
    n = 10000
    print(f'Total Lychrel numbers below {n}: {count_lychrel_range(n, 50)}')
    print(f'Time: {time() - start_time} seconds.')
