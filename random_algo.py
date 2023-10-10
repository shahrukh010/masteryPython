import time

def generate_random_1_digit():
    #current_time = int(time.time() * 1000)
    current_time =int(time.time_ns());
    random_number = (current_time % 49) + 1
    return random_number

random_number = generate_random_1_digit()

print(f"Random 1-Digit Number: {random_number}")

