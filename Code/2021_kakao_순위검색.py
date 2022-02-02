def lower_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:  # left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return right

li = [1,2,3,4,5,6,7,8,9,11,12]

print(lower_bound(li, 10))