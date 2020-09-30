import random
import string


def get_random_string(length):
    # Create random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str