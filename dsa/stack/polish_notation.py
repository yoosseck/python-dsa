from stack import Stack


def polish_notation(expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])

    # Split the expresison into tokens
    tokens = expression.split()

    for token in reversed(tokens):

        if token not in operators:
            # Push operand to stack
            stack.push(int(token))
        else:
            # Pop 2 operands from stack
            operand1 = stack.pop()
            operand2 = stack.pop()

            print('op1', operand1)
            print('op2', operand2)

            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            elif token == "/":
                result = operand1 / operand2

            stack.push(result)

    print(expression)
    print(result)


# if __name__ == "__main__":
#     expression = "+ 9 * 2 3"
#     polish_notation(expression)
