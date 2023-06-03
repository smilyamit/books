#eg for generator

def count_num(n):
    while n>0:
        yield n
        n -= 1


for i in count_num(5):
    print(i)
