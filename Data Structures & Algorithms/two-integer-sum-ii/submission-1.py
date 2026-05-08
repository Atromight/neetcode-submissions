class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        n = len(numbers)
        while True:
            if j == n:
                i += 1
                j = i + 1
                continue

            nums_sum = numbers[i] + numbers[j]
            if nums_sum < target:
                j += 1
            elif nums_sum == target:
                return [i+1, j+1]
            elif nums_sum > target :
                i += 1
                j = i + 1
            
            
            


        