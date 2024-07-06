import random
import sys


def get_numbers_ticket(min_value, max_value, quantity):

    numbers_ticket = []

    try:
        if min_value < 1 or max_value > 1000:
            raise ValueError("min and max must be between 1 and 1000")

        if min_value > max_value:
            raise ValueError("min must be less or equal than max")

        if max_value - min_value < quantity - 1:
            raise ValueError("Difference between max and min must be greater than quantity - 1")

        if min_value == max_value:
            return [min_value]

        possible_values = list(range(min_value, max_value + 1))

        for i in range(0, quantity):
            index = random.randint(0, len(possible_values) - 1)
            value = possible_values[index]
            del possible_values[index]
            numbers_ticket.append(value)

    except ValueError as error:
        sys.stderr.write(str(error))

    return numbers_ticket


print(get_numbers_ticket(10, 50, 300))
