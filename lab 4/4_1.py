from itertools import combinations

class SubsetGenerator:
    def __init__(self, nums):
        self.nums = nums

    def get_subsets(self):
        subsets = [[]]  # Start with the empty subset
        for i in range(1, len(self.nums) + 1):
            subsets.extend(list(combinations(self.nums, i)))
        return subsets

# Example usage
sg = SubsetGenerator([1, 2, 3])
print(sg.get_subsets())
