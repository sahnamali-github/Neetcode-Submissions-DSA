class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res = [0]*len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break
        # return res

        # stack = []
        # res = [0]*len(temperatures)
        # for i,t in enumerate(temperatures):
        #     while stack and t > temperatures[stack[-1]]:
        #         m = stack.pop()
        #         res[m] = i - m
        #     stack.append(i)
        # return res


        stack = []   #[[temp, index]]
        res = [0]*len(temperatures)     
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp,index = stack.pop()
                res[index] = i - index
            stack.append([t,i])
        return res
            
          



                
                 
            

                



        