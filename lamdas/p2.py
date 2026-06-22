# n number of arguments

import sys
total = lambda *n: sum(n)

def main():
    print("result:", total())
    print("result:", total(10))
    print("result:", total(10,20))

    print("result:", total(10,20,30))
    print("result:", total(10,20,30,40))
    print("result:", total(10,20,30,40,50))

sys.exit(main())
    
