# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer. The digits are
# ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# SOLUTION:
# Increment last element by one, then increment (or not) other elements
# in right-left order based on standard math addition rules.
# If number order of the whole large integer increases, we add element 0
# to the end of the list

class Solution(object):
    def plusOne(self, digits):
        plus = 1
        counter = len(digits) - 1
        while plus > 0:
            curr = digits[counter] + plus
            digits[counter] = curr % 10
            plus = curr // 10
            if counter == 0 and plus == 1:
                digits[counter] = 1
                digits.append(0)
                plus = 0
            counter -= 1
        return digits


if __name__ == '__main__':
    incrted = Solution()
    print(incrted.plusOne([1, 2, 3]))
    print(incrted.plusOne([9, 9, 9, 9, 9]))