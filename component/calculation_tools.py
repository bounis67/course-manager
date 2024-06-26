import os

def generate_numbers(n):
    """
    Generate a list of numbers from 1 to n.

    Args:
        n (int): The upper limit of the range.

    Returns:
        list: A list of numbers from 1 to n, with leading zeros if necessary.
    """
    number_list = []
    for i in range(1, n + 1):
        number_str = str(i).zfill(2)
        number_list.append(number_str)
    return number_list
