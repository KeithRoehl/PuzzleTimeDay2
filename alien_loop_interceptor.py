import random

def alien_loop():
    def safeguard():
        global alien_loop
        alien_loop = original_loop  # Resets the function if tampered with

    original_loop = alien_loop  # Preserve the original definition

    while True:
        safeguard()  # Restore to original on each iteration
        code = random.choice([
            "x = 5",
            "y = x + 2",
            "print('Alien server running...')",
            "z = y * 10"
        ])
        exec(code)

# Uncomment this to start the loop!
# alien_loop()
