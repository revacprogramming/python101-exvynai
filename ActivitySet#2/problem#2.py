def input_two_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a, b

def add(a, b):
    return a + b


def output(a, b, sum):
    print(a, "+", b, "=", sum)


def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
