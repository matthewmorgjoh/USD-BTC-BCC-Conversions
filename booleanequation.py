import copy
import sys

print("This program reads boolean equations and outputs the truth table.")
print("You may use the operators ~, ∨, and ∧, or")
print("their text equivalents, not, or, and and.")
print("You may use parenthesis, braces, and brackets to group your equations,")
print("and you must use single letters for your variable names, as 'a∨b'\n")

equation = input()
equation_copy = equation
equation_vars = []
equation = " " + equation + " "
equation = equation.replace("~", " not ")
equation = equation.replace("∨", " or ")
equation = equation.replace("∧", " and ")
equation = equation.replace("[", "(")
equation = equation.replace("]", ")")
equation = equation.replace("{", "(")
equation = equation.replace("}", ")")

for index in range(len(equation)):
    if equation[index] in " ()^":
        continue
    if equation[index + 1] in " ()" and equation[index - 1] in " ()" and equation[index] not in equation_vars:
        equation_vars.append(equation[index])

equation_vars.sort()

for equationIndex in equation_vars:
    sys.stdout.write(equationIndex + '\t')

print(equation_copy)

for equationIndex in range(pow(2,len(equation_vars))):
    vals = str(bin(equationIndex)).replace('0b','').zfill(len(equation_vars))

    for value in vals:
        sys.stdout.write(value + '\t')

    equation_vars_copy = copy.deepcopy(equation_vars)
    for index in range(len(equation_vars_copy)):
        equation_vars_copy[index] += " = " + vals[index]
        exec(equation_vars_copy[index])

    truthTable = "result = equation"
    truthTable = truthTable.replace('equation', equation)
    exec(truthTable)
    if result:print(1)
    else:print(0)

