class Father: 
	def func1(self):
		print("From father")
  
# Base class2 
class Child1(Father): 
	def func2(self):
		print("From child1")

class Child2(Father): 
    def func3(self): 
    	print("from child2")


  
# Derived class 
class Child3(Father): 
    def func4(self): 
    	print("from child3")
  
# Driver's code 
k1= child1()
k2= child2()
k3 = child3()
k1.func1()
k2.func1()
k3.func1()