class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    
        holder = [0 for _ in range(len(temperatures))]
        temp = []
        for i in range(0, len(temperatures)):
          while (len(temp)>0) and temperatures[i]> temperatures[temp[len(temp)-1]]:
              index = temp[len(temp)-1]
              temp.pop()
              holder[index] = i-index
          temp.append(i)
        return list(holder)
     