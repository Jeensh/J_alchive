import sys
input = sys.stdin.readline

def print_all(to_print):
    for p in to_print:
        print(p, end=' ')
    print()

def recur(num, dept, to_print):
    if dept == (M + 1):
        print_all(to_print)
    else:
        tmp = list(to_print)
        for i in range(num + 1, N + 1):
            to_print = list(tmp)
            to_print.append(i)
            num = i
            recur(num, dept + 1, to_print)


if __name__ == "__main__":
     N, M = map(int, input().split())
     recur(0, 1, [])