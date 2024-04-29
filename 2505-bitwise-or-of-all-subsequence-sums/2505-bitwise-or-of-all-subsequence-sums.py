class Solution:
    def subsequenceSumOr(self, nums: list[int]) -> int:
        or_ = 0
        for bit in range(60):
            sum_, tail = 0, (1 << (bit + 1)) - 1
            for num in nums:
                sum_ += num & tail
            if sum_ >= 1 << bit:
                or_ |= 1 << bit
        return or_