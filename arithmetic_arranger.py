# freeCodeCamp - Scientific Computing with Python
# https://www.linkedin.com/in/vasilis-timoudas
# https://github.com/vasilis-timoudas

def arithmetic_arranger(problems, solutions=False):
    # There are more than 5 problems (the limit is 5)
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize the lines
    line1, line2, line3, line4 = "", "", "", ""

    # Use loop per problem
    for i, problem in enumerate(problems):
        num1, op, num2 = problem.split()

        # The appropriate operators aren't addition and subtraction
        if not op in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Each number don't contains digits
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        # Each operand has more than four digits
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Addition
        if op == "+":
            res = int(num1) + int(num2)
        # Subtraction
        else:
            res = int(num1) - int(num2)

        # Maximum length between num1 and num2
        num_length = len(max([num1,num2], key=len))

        # Built the solution per line
        line1 += num1.rjust(num_length + 2)
        line2 += op + num2.rjust(num_length + 1)
        line3 += "-" * (num_length + 2)
        line4 += str(res).rjust(num_length + 2)

        # Add space per line except the last problem
        if i < len(problems) - 1:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            line4 += "    "

    arranged_problems = line1 + "\n" + line2 + "\n" + line3

    # If true add the solutiion
    if solutions:
        arranged_problems += "\n" + line4

    return arranged_problems
