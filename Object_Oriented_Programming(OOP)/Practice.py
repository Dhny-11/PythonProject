class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car('Toyota', 'red')
car2 = Car('Lambo', 'green')

print('Car 1 Brand:', car1.brand) 
print('Car 1 Color:', car1.color) 

print('Car 2 Brand:', car2.brand) 
print('Car 2 Color:', car2.color) 

print('-------------------------------')
print('\n')

class wallet: 
    def __init__(self, balance):
        self.__balance = 0
        
        
    def __validate(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        
    def deposit(self, amount):
        self.__validate(amount)
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__validate(amount)
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        
    def get_balance(self):
        return self.__balance
    
account1 = wallet(1000)
print('Initial Balance:', account1.get_balance())
account1.deposit(500)
print('Balance after deposit:', account1.get_balance())
account1.withdraw(200)
print('Balance after withdrawal:', account1.get_balance())

account2 = wallet(1000)
account2.deposit(2000)
print('Initial Balance:', account2.get_balance())   


print('-------------------------------')
print('\n')


class Circle:
    def __init__(self, radius):
        self.radius = radius # Calling the setter

    @property
    def radius(self):  # A getter to get the radius
        return self._radius

    @radius.setter
    def radius(self, value):  # A setter to set the radius
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value

    @radius.deleter 
    def radius(self): 
        print('Deleting radius...')
        del self._radius
    
    
my_circle = Circle(3)
print('Initial radius:', my_circle.radius) # Initial radius: 3

my_circle.radius = 8
print('After modifying the radius:', my_circle.radius) # After modifying the radius: 8


# Create circle object with a radius
my_circle = Circle(33)
print("Initial radius:", my_circle.radius)  # Initial radius: 33

# Delete the radius
# This calls the deleter
del my_circle.radius # Deleting radius...
print("Radius deleted!") # Radius deleted!



print('\n')

class animal:
    def __init__(self,name):
        self.name = name
        
    def sound(self):
        return f'{self.name} make a sound'
    

class Dog(animal):
    bark = 'Woof woof '
    
    
    def sound(self):
        base = super().sound()
        return f'{base}, then {self.name} barks {self.bark}'
    
jack = Dog('Jack')
print(jack.sound())
#print(jack.bark)