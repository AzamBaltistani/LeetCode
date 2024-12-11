# time limit exceeded by using bruteforce


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[i]+numbers[j] == target:
                    return [i+1, j+1]



sol = Solution()


numbers = [2,7,11,15]
target = 9

print(sol.twoSum(numbers, target))