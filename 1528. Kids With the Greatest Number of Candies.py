class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = 0
        result = []

        for num in candies:
            max_candy = max(max_candy, num)

        return [num + extraCandies >= max_candy for num in candies]