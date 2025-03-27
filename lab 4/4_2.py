class PairFinder:
    def __init__(self, nums):
        self.nums = nums

    def find_pair(self, target):
        seen = {}
        for i, num in enumerate(self.nums):
            complement = target - num
            if complement in seen:
                return (seen[complement], i)  # Return indices
            seen[num] = i
        return None  # No pair found

# Example usage
pf = PairFinder([2, 7, 11, 15])
print(pf.find_pair(9))  # Output: (0, 1)
