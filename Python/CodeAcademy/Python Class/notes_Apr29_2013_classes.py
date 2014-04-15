"""Notes Apr 29 2013"""
"""basic class"""
class Point3D(object):
	#define initialization method
    def __init__(self, num1, num2, num3):
        self.x = num1
        self.y = num2
        self.z = num3 
    
    #define representation method, so you can just "print Object"
    def __repr__(self):    
        return "(%s, %s, %s)" % (str(self.x),str(self.y),str(self.z))


myPoint = Point3D(1,2,3)

#this works due to the __repr__ definition
print myPoint


"""advanced class with inheritance, overriding and superclass access"""
class Employee(object):
	"""Models real-life employees!"""
	def __init__(self, employee_name):
		self.employee_name = employee_name
	
	def calculate_wage(self, hours):
		self.hours = hours
		return hours * 20.00

# this is a subclass of Employee superclass
class PartTimeEmployee(Employee):
    #override the calculate wage method of the superclass for lower wage
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    
    #if there just happens to be a parttimer that gets full time wage
    #access the superclass method for wage
    #still needs the same arguments as the superclass method
    def full_time_wage(self, hours):
    	#return the super call with this subclass.superclass method
        return super(PartTimeEmployee, self).calculate_wage(hours)
        
milton = PartTimeEmployee("Milton")
print milton.full_time_wage(10)

"""the above superclass access in simple terms"""
class DerivedClass(Base):
   def some_method(self):
   	#meth is the method from the bass (super) class
       super(DerivedClass, self).meth()