from typing import List


def search(nums: List[int], target: int) -> int:
    right = len(nums) - 1  # 右指针，指向列表最大下标
    left = 0    # 左指针，指向列表最小下标
    pointer = right // 2    # 指针指向中央元素，若列表有偶数个，则指向中央偏小元素
    res = -1    # 指定返回值，默认为1
    while True:
        if nums[pointer] == target:
            res = pointer
            break
        elif right - left <= 1:
            if nums[right] == target:  # 解决只有两个元素，且taget在下标位1的位置的极端条件
                res = right
            break
        if nums[pointer] > target:  # 小于目标值，往左边找
            right = pointer
            pointer = (left + pointer) // 2
        elif nums[pointer] < target:    # 搭于目标值，往右边找
            left = pointer
            pointer = (pointer + right) // 2
            if left == pointer and right != 0:
                pointer = pointer + 1   # 因为类似5+6//2==5，这句操作防止最后一个下标的位置没有被查找到
    return res
