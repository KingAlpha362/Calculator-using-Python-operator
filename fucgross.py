import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

x = float(input("Enter a number: "))
op = input("Enter an operator: (+, -, *, /) ")
y = float(input("Enter a number: "))

if op in ops:
    result = ops[op](x, y)
    print(f"The answer is {result}")
else:
    print("Invalid operator.")