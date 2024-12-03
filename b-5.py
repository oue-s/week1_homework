def value_total(nums):
    total = 0
    for i in nums:
        total += i
    return total


def value_max(nums):
    max = 0
    for i in nums:
        if max < i:
            max = i
    return max


def value_min(nums):
    min = nums[0]
    for i in nums:
        if min > i:
            min = i
    return min


def value_ave(nums):
    return value_total(nums) // len(nums)


line = input("データを入力してください(スペース区切り)")
line_s = line.split(" ")

nums = []
for i in line_s:
    nums.append(int(i))

print("合計値:", value_total(nums))
print("最大値:", value_max(nums))
print("最小値:", value_min(nums))
print("平均値:", value_ave(nums))
