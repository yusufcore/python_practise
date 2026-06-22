
import sys

def square(x):
    return x*x

sqr = lambda x: x*x

def main():
    result = square(10)
    print('Square = ', result)

    print("------------------Using lambda fn for squaring------------------------")

    print('Square using lambda fn:', sqr(10))

    numbers = [1,2,3,4,5]
    print("list of numbers:", numbers)

    square_list = list(map(sqr, numbers))
    print("square list :", square_list)
    
if __name__ == "__main__":
    sys.exit(main())