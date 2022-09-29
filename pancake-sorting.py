class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        
        arr2 = arr.copy()
        arr2.sort()
        if arr2 == arr:
            return []
        
        size = len(arr)
        answer = []
        for a in reversed(range(1,size+1)):
            current = arr.index(a)
            if current == a-1:
                continue
            if current != 0:
                answer.append(current+1)
                arr[: current+1] = reversed(arr[: current+1])
            answer.append(a)
            arr[:a] = reversed(arr[:a])

        return answer