import random


def generate_random_number(min_value, max_value):
    """
    Generates a random integer between min_value and max_value (inclusive).

    Args:
        min_value (int): The minimum integer value.
        max_value (int): The maximum integer value.

    Returns:
        int: A randomly generated integer.
    """
    return random.randint(min_value, max_value)


def get_random_operator():
    """
       Randomly selects a mathematical operator from a list of '+', '-', and '*'.

       Returns:
           str: A randomly selected operator.
    """
    return random.choice(['+', '-', '*'])


def generate_problem_and_solution(num1, num2, operator):
    """
        Creates a math problem based on two numbers and an operator,
        and calculates the correct answer.

        Args:
            num1 (int): The first number.
            num2 (int): The second number.
            operator (str): The math operator ('+', '-', or '*').

        Returns:
            tuple: A tuple containing:
                - str: The math problem in string format.
                - int: The correct answer to the problem.
     """
    problem = f"{num1} {operator} {num2}"     # Format the math problem as a string

    # Calculate the answer based on the operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    return problem, answer


def math_quiz():
    """
    Runs a math quiz game where the user is presented with math problems
    and must provide the correct answers to earn points.

    The game ends after a set number of questions, and the final score is displayed.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):    # Loop to present a set number of questions to the user
        num1 = generate_random_number(1, 10);
        num2 = generate_random_number(1, 5);
        operator = get_random_operator()

        problem, correct_answer = generate_problem_and_solution(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        user_answer = input("Your answer: ")

        # Error handling for invalid user input (e.g., non-integer answers)
        try:
            user_answer = int(user_answer) # Ask for the user's answer and convert it to an integer
        except ValueError:
            # Handle the case where the input is not an integer
            print("Invalid input. Please enter an integer.")

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
