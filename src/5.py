def get_random_code(length=10):
    """Generate a random string of letters and digits"""
    import random
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(characters) for i in range(length))
