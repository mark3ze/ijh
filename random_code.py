import random
import math
import time
from datetime import datetime

class RandomGenerator:
    def __init__(self):
        self.seed = random.randint(1, 1000)
        random.seed(self.seed)
    
    def generate_random_list(self, size=10):
        return [random.randint(1, 100) for _ in range(size)]
    
    def calculate_stats(self, numbers):
        return {
            'mean': sum(numbers) / len(numbers),
            'max': max(numbers),
            'min': min(numbers),
            'sum': sum(numbers)
        }
    
    def random_pi_approximation(self, iterations=100000):
        inside_circle = 0
        for _ in range(iterations):
            x = random.random() * 2 - 1
            y = random.random() * 2 - 1
            if x*x + y*y <= 1:
                inside_circle += 1
        return 4 * inside_circle / iterations

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def random_color_generator():
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan']
    return random.choice(colors)

def main():
    print(f"Random Code Generator - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    gen = RandomGenerator()
    
    # Generate random numbers
    numbers = gen.generate_random_list(15)
    print(f"Random numbers: {numbers}")
    
    # Calculate statistics
    stats = gen.calculate_stats(numbers)
    print(f"Statistics: {stats}")
    
    # Pi approximation
    pi_approx = gen.random_pi_approximation(50000)
    print(f"Pi approximation: {pi_approx} (actual: {math.pi})")
    
    # Fibonacci sequence
    fib_sequence = list(fibonacci_generator(10))
    print(f"Fibonacci sequence: {fib_sequence}")
    
    # Random colors
    random_colors = [random_color_generator() for _ in range(5)]
    print(f"Random colors: {random_colors}")
    
    # Random delay simulation
    print("Simulating random delays...")
    for i in range(3):
        delay = random.uniform(0.1, 0.5)
        time.sleep(delay)
        print(f"  Delay {i+1}: {delay:.2f} seconds")

if __name__ == "__main__":
    main()
