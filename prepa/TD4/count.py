from math import factorial as fac
# https://forums.futura-sciences.com/mathematiques-college-lycee/193661-repartir-n-objets-k-boites.html
def binomial(x, y):
    try:
        return fac(x) // fac(y) // fac(x - y)
    except Exception:
        return 0

def main():
    S, K = map(int, input().split())
    minimums = list(map(int, input().split()))
    margin = S - sum(minimums)
    print(binomial(margin + K - 1, margin))
if __name__ == '__main__':
    main()