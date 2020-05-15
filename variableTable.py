
"""
-----------------VARIABLE TABEL--------------------------
result[]:["1", "2", "fizz", "4", "buzz","fizz", "fizz","7","8","fizz","buzz", "11","fizz","13","14", "fizzbuzz"]
i: 1,2,3,4,5,6,7,8,9,10
n: 10
"""

class Solution(object):
    def fizzBuzz(self, n):

        i = 1 
        result = [] 
        while (i<=n):
            if i %15 == 0:
                result.append('FizzBuzz')
            elif i%5 == 0:
                result.append('Buzz')
            elif i % 3 == 0:
                result.append('Fizz')
            else:
                result.append(str(i))
            i = i + 1
        return result

if __name__ == '__main__':
    s = Solution()
    print "The Output is : " + str(s.fizzBuzz(10))