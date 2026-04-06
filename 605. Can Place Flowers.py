class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if n == 0:
                break

            if flowerbed[i] == 1:
                continue

            if i - 1 >= 0:
                if flowerbed[i-1] == 1:
                    continue
            
            if i + 1 < len(flowerbed):
                if flowerbed[i+1] == 1:
                    continue

            n = n - 1
            print(i)

            flowerbed[i] = 1

        return n == 0
