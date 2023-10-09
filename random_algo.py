import time

def generate_random_1_digit():
    current_time = int(time.time())
    random_number = (current_time % 49) + 1
    return random_number

random_number = generate_random_1_digit()

print(f"Random 1-Digit Number: {random_number}")

