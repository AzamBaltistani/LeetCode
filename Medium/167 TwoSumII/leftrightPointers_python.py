class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers)-1
        for i in range(len(numbers)):
            x = numbers[left] + numbers[right]
            if x == target:
                return [left+1, right+1]
            
            if x < target:
                left += 1
            else:
                right -= 1



sol = Solution()


numbers = [2,7,11,15]
target = 9

print(sol.twoSum(numbers, target))