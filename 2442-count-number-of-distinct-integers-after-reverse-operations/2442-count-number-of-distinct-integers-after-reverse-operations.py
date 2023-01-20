class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        temp = []
        for num in nums:
            temp.append(Solution.reverse(num))
        return(len(set(nums+temp)))  

    def reverse(number):
        reversed_num = 0
        while number != 0:
            digit = number % 10
            reversed_num = reversed_num * 10 + digit
            number //= 10
        return reversed_num

        