#!/usr/bin/env python


def main():
    maxVal = 20
    sum = 0

    for i in range(0, maxVal + 1):
        sum = sum + i
        print(sum, i)

    print(f"This is sum: {sum}")


if __name__ == "__main__":
    main()
