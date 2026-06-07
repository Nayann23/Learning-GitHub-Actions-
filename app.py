import random
import pandas


print("Hello")
print("Program Started")

x = 10 / 0

print("Program Finished")

secret_number = random.randint(1, 10)
guess = 7

print(f"Secret Number: {secret_number}")
print(f"Guess: {guess}")

if guess == secret_number:
    print("🎉 Correct Guess!")
else:
    print("❌ Wrong Guess!")