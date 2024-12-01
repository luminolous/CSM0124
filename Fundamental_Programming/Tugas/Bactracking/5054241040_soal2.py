class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        array = []

        def combination(value):
            if len(array) == k:
                result.append(array[:])
                return
            
            for num in range(value, n + 1):
                array.append(num)
                combination(num + 1)
                array.pop()

        combination(1)
        return result