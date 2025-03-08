def get_random_string(length):
    import random
    import string

    # Define the list of characters to use in the string
    chars = string.ascii_letters + string.digits

    # Generate a random string of the given length
    return ''.join(random.choice(chars) for _ in range(length))

# Example usage:
print(get_random_string(10))
