# https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=666

from functools import reduce

def allDifferent(*args):
    strnum = reduce(lambda acc, actual: acc + f'{actual:05}', args, "")
    for i in range(0, len(strnum)):
        for j in range(0, len(strnum)):
            if i != j:
                if strnum[i] == strnum[j]:
                    return False
    return True

def solution(n):
    pairs = []
    errormsg = f"There are no solutions for {n}."
    if (n == 0):
        return errormsg

    for div in range(1234, 98765):
        mult = n * div
        if (allDifferent(div, mult)):
            pairs.append(f"{mult:05} / {div:05} = {n}")

    if (len(pairs) == 0):
        return errormsg
    return pairs

solv = solution(int(input()))

if (isinstance(solv, list)):
    for x in solv:
        print(x)
else:
    print(solv)