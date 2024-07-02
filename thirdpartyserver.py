from flask import Flask, jsonify
import random

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime():
    while True:
        num = random.randint(2, 100)
        if is_prime(num):
            return num

def generate_fibonacci():
    a, b = 0, 1
    for _ in range(random.randint(1, 10)):
        a, b = b, a + b
    return a

def generate_even():
    return random.choice([i for i in range(2, 101) if i % 2 == 0])

def generate_random():
    return random.randint(1, 100)

@app.route('/numbers/<number_type>', methods=['GET'])
def get_number(number_type):
    # Example implementation to return requested number type
    if number_type == 'prime':
        number = 17  # Example: Generate prime number
    elif number_type == 'fibonacci':
        number = 34  # Example: Generate Fibonacci number
    elif number_type == 'even':
        number = 16  # Example: Generate even number
    elif number_type == 'random':
        number = 42  # Example: Generate random number
    else:
        return jsonify({"error": "Invalid number type"}), 400

    return jsonify({"number": number})
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
