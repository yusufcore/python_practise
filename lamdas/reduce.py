
from functools import reduce

salaries = [300, 400, 200, 200, 450]

total = lambda x=0,y=0: x+y

print("total salaries: ", reduce(total, salaries))