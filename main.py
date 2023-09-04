from functionality import print_title
from functionality import Options

def main():
    print_title()

    first_value = float(input("Input first value:\n>>> "))
    second_value = float(input("Input second value:\n>>> "))
    sign_value = input("Input sign (+, -, /, *):\n>>> ")
    while sign_value not in ["+", "-", "/", "*"]:
        sign_value = input("Value invalid, please try again:\n>>> ")

    actions = {"+": Options.plus, "-":Options.minus, "*":Options.multiply, "/":Options.divide}
    func = actions[sign_value]
    result = func(first_value, second_value)
    
    print("\nResult: {}".format(result))

    input("\nPress any key to exit...")
    



if __name__ == "__main__":
    main()