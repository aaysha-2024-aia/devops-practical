def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


# Example usage
nums = [1, 1, 2, 2, 3, 4, 4]
new_length = remove_duplicates(nums)

print("New Length:", new_length)
print("Updated List:", nums[:new_length])
