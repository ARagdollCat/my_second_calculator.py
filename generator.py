main_file = open("main.py", "w")

min_num = int(-50)
max_num = int(50)
nums = range(min_num, max_num + 1)
signs = ["+", "-", "*", "/", "^", "%", "&", "|", "~"]

main_file.write(f"""print("Welcome to my second calculator!") # type: ignore
print("It can add, subtract, multiply, divide, and more from {min_num} to {max_num}")

first_num = int(input("Type the first number: "))
sign = input("Choose a sign (+, -, *, /, ^, %, &, |, ~): ") 
last_num = int(input("Type the last number: "))
""")

for first_num in nums:
    for last_num in nums:
        for sign in signs:
            equation = f"{first_num} {sign} {last_num}"
            try:
                if sign == "~":
                    equals = ~first_num
                else:
                    equals = eval(equation.replace("^", "**").replace("/", "//"))
            except ZeroDivisionError:
                equals = "Undefined"

            main_file.write(f"""if first_num == {first_num} and sign == "{sign}" and last_num == {last_num}:
    print("{first_num} {sign} {last_num} = {equals}")\n""")

            
main_file.close()