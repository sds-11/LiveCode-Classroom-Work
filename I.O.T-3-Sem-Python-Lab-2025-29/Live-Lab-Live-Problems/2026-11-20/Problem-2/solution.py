# LiveCode Classroom - Solution
# Batch: I.O.T 3 Sem Python Lab  2025-29
# Category: Live Lab Problems
# Question: Problem 2 (Solve the error)
# Score: Submitted (Evaluation Completed)
# Synced: Friday, November 20, 2026 at 10:07 AM

# Write your Python solution below
class student :
    def __init__(self,name):
        self.name = name
    def greet(self):
        return(f"Hello {self.name} ,How are you??")
obj = student("Vivek")
obj1 = student("Anuj")
print(obj.greet(),sep=" ")
print(obj1.greet())