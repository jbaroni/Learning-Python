def binary_search(seq, item):
    begin_index = 0
    end_index = len(seq)-1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index- begin_index) // 2
        midpoint_val = seq[midpoint]
        if midpoint_val == item:
            return midpoint
        elif item < midpoint_val:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None

sequence_a = [2,4,5,6,7,8,12,15,17,19]

item_a = 12


print(binary_search(sequence_a, item_a))

# Alternatively
""" def search(self, nums, target):
        L = 0
        R = len(nums)-1
        while L <= R:
            m = (L + R) // 2

            # Case 1
            if nums[m] == target:
                return m

            # Case 2
            elif nums[m] < target:
                L = m + 1

            # Case 3
            elif nums[m] > target:
                R = m - 1

         # If search finishes without finding target, return -1.       
        return -1 """