import random
import operator


DESCRIPTION = 'What is the result of the expression?'


def generate_question():
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operations = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    op_symbol, op_func = random.choice(operations)
    question = f'{num1} {op_symbol} {num2}'
    correct_answer = str(op_func(num1, num2))
    return question, correct_answer


def play_round():
    question, correct_answer = generate_question()
    return question, correct_answer
