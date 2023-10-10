def my_steps(n):
    if not (1 <= n <= 25):
        raise ValueError("Input must be between 1 and 25 (inclusive)")

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2

        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n]
