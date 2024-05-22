# quotes.py

import random

# List of quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Stay hungry, stay foolish. - Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It always seems impossible until it is done. - Nelson Mandela",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The only thing we have to fear is fear itself. - Franklin D. Roosevelt",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "Life is what happens when you're busy making other plans. - John Lennon"
]

def generate_random_quote():
    """Generate a random quote from the list"""
    return random.choice(quotes)

if __name__ == "__main__":
    print(generate_random_quote())
