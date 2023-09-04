#prints title of the program
def print_title():
    title = "| Python simple calculator for evoacademy |"
    title_len = len(title)
    print("="*title_len)
    print(title)
    print("="*title_len)

#all options
class Options:
    def plus(a, b):
        return a + b

    def minus(a,b):
        return a - b

    def multiply(a,b):
        return a*b
    
    def divide(a,b):
        return a/b