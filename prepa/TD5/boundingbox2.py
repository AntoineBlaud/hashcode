
def main():
    n = int(input())
    xmin, ymin = xmax, ymax, = tuple(map(int, input().split(" ")))
    for _ in range(n - 1):
        x , y = tuple(map(int, input().split(" ")))
        xmax, ymax, xmin, ymin = max(x, xmax), max(y, ymax), min(x, xmin), min(y, ymin)
    print(abs(xmax - xmin), abs(ymax - ymin))

if __name__ == '__main__':
    main()
