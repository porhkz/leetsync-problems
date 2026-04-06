class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = 0
        result = []

        for num in candies:
            max_candy = max(max_candy, num)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)

        return result