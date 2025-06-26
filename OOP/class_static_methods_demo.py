class Calculator:
    calculation_type = "arithmetic operation"
   
    @staticmethod
    def add(a , b):
        return a + b
    
    @classmethod 
    def multiply(cls, a, b):
        print(f"calculation type: {cls.calculation_type}")
