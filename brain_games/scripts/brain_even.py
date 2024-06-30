import random
import prompt

def is_even(number):
    return number % 2 == 0

def play_round():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    print(f'Question: {number}')
    user_answer = prompt.string('Your answer:' )
    if user_answer.lower() == correct_answer:
        print('Correct!')
        return True
    else: 
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False
    
def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    rounds_count = 3
    for _ in range(rounds_count):
        if not play_round():
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulation, {name}!")

if __name__ == '__main__':
    main()