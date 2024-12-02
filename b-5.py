line = input("データを入力してください(スペース区切り)")
line_s = line.split(" ")

nums = []
for i in line_s:
    nums.append(int(i))

total = 0
max = 0
min = nums[0]
for i in nums:
    total += i
    if max < i:
        max = i
    if min > i:
        min = i

print("合計値:", total)
print("最大値:", max)
print("最小値:", min)
print("平均値:", total // len(nums))
