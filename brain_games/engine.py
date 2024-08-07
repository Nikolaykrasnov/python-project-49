import prompt

MAX_ROUNDS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)

    for _ in range(MAX_ROUNDS):
        question, correct_answer = game.play_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"""
                '{user_answer}' is wrong answer ;(.
                Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!""")
            return

    print(f'Congratulations, {name}!')
