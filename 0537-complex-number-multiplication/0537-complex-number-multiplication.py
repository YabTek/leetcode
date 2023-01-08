class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:  
        num1 = num1.split("+")
        num2 = num2.split("+")
        n1 = int(num1[0])
        n2 = int(num1[1][:-1])
        n3 = int(num2[0])
        n4 = int(num2[1][:-1])
        
        real = (n1*n3) - (n2*n4)
        imaginary = (n1*n4) + (n2*n3)
        
        return str(real) + "+" + str(imaginary) + "i"
        

                

        
            
        
        

