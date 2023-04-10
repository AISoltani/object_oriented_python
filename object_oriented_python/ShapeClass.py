class Shape:
    size = 2
    def __init__(self, name, color):
      self.name = name
      self.color = color
      
   
shape1 = Shape('Circle','Yellow')
shape2 = Shape('Square','Green')

print(shape1.name)
print(shape2.color)

shape1.color = 'blue'
shape1.radius = 20


print(shape1.color)
print(shape1.radius)
print(shape1.name)

print(hasattr(shape2, 'radius')) # Returns true if 'radius' attribute exists
print(getattr(shape1, 'radius')) # Returns value of 'radius' attribute 
setattr(shape2, 'radius', 8) # Set attribute 'radius' at 8
print(shape2.radius)
delattr(shape1, 'color') # Delete attribute 'color'
#print(shape1.color)

del shape1.name
print(shape1.name)
    
    
