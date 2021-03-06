# Day 17 coding challenge - More exceptions

# Write a Calculator class with a single method: int power(int,int). The power method takes two integers, n and
# p, as parameters and returns the integer result of n**p. If either n or p is negative, then the method must throw
# an exception with the message: n and p should be non-negative.

class Calculator:
    def power(self, n, p):
        try:
            if n < 0:
                return 'n and p should be non-negative'
            elif p < 0:
                return 'n and p should be non-negative'
        except ValueError:
            return 'Not an integer'
        ans = n**p
        return ans



myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)