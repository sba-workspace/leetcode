class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        result = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            d1 = int(num1[i])
            for j in range(m - 1, -1, -1):
                d2 = int(num2[j])
                pos = i + j + 1
                total = d1 * d2 + result[pos]

                result[pos] = total % 10
                result[pos - 1] += total // 10

        idx = 0
        while idx < len(result) and result[idx] == 0:
            idx += 1

        return "".join(map(str, result[idx:]))