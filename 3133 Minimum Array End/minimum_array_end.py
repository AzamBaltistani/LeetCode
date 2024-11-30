def minEnd(n, x):
    """
    :type n: int
    :type x: int
    :rtype: int
    """
    nums = []
    for i in range(n):
        nums.append(i)

    merge = 0
    for i in range(len(nums) - 1):
        merge = nums[i] & nums[i+1]

    print(merge)
    print(merge & x)
    return nums


nums = minEnd(3,4)
print(nums)