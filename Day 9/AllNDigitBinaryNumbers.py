def recur(n, left="", right="", diff=0):
    if n > 9:
		return
    if n > 0 and (2 * abs(diff) <= n):
        if n == 1:
			recur(0, left, '0' + right, diff)
			recur(0, left, '1' + right, diff)
			return
        if left != "":
			recur(n - 2, left + '0', right + '0', diff)
            recur(n - 2, left + '0', right + '1', diff - 1)
        recur(n - 2, left + '1', right + '0', diff + 1)
		recur(n - 2, left + '1', right + '1', diff)
    elif n == 0 and diff == 0:
		print(left + right, end=' ')


if __name__ == '__main__':
    # N-digit number
	n = 6

	recur(n)
