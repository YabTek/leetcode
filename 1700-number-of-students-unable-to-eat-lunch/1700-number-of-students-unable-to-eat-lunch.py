class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stk = sandwiches[::-1]
        
        while stk:
            top_sandwich = stk[-1]
            front_student = students[0]
            
            if top_sandwich not in students:
                break
            elif top_sandwich == front_student:
                students.pop(0)
                stk.pop()
            else:
                front = students.pop(0)
                students.append(front)
                
        return len(students)
                
                
                
        