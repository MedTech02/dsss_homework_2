import unittest
from math_quiz import generate_random_number, get_random_operator, generate_problem_and_solution


class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        """Test if the generated operator is one of the allowed operators (+, -, *)"""
        allowed_operators = {'+', '-', '*'}
        for _ in range(1000):  # Test multiple times to ensure all operators can be selected
            operator = get_random_operator()
            self.assertIn(operator, allowed_operators, f"Operator {operator} is not valid")

    def test_generate_problem_and_solution(self):
        """Test if the generated problem and solution is as expected"""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 3, '*', '4 * 3', 12)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_problem_and_solution(num1, num2, operator)
            self.assertEqual(problem, expected_problem,
                             f"Expected problem '{expected_problem}' but got '{problem}'")
            self.assertEqual(answer, expected_answer, f"Expected answer {expected_answer} but got {answer}")


if __name__ == "__main__":
    unittest.main()
