from functools import reduce

def collatz(starting_num):
    nums = []
    num = starting_num
    while num > 1:
        num = (num // 2) if num % 2 == 0 else (3 * num//2 + 1)
        nums.append(num)

    return nums

n1, n2 = map(int, input().split(" "))
collatz_n1, collatz_n2 = collatz(n1), collatz(n2)
collatz_set = set(collatz_n1).intersection(collatz_n2)
c1 = sorted(collatz_set, key=collatz_n1.index)
print(c1[0], max(collatz_set))