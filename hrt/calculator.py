"""Notes:
- calc performs *operations* on *expressions*.
- expressions can be of two types: 1. Lit 2. Var
    - immediately i understand that i could probably have an expressions class
      that would have two child classes as Lit and Var
- operations can be of the type:
    - adding
    - subtracting
    - multiplying
    - operations would always be performed on *two* expressions.
        - so how would i handle (1+2)+3
"""


class Expression:
    def __init__(self):
        pass
    
    def toString(self)-> str:
        print("Wrong Method:Returning from expressions class")
        return "" 

    def simplify(self):
        return self

    def Add(self, other):
        return AddExpression(self, other)

    def Sub(self, other):
        return SubExpression(self, other)

    def Mul(self, other):
        return MulExpression(self, other)

class Lit(Expression):
    def __init__(self, value:int) -> None:
        self.value = value

    def toString(self)-> str:
        return str(self.value)

    def simplify(self):
        return self

class Var(Expression):
    def __init__(self, value:str) -> None:
        self.value = value

    def toString(self):
        return self.value

    def simplify(self):
        return self

class BinaryExpression(Expression):
    def __init__(self, left, right, operator:str):
        self.left = left 
        self.right = right
        self.operator = operator

    def evaluate():
        pass

    def toString(self):
        return f"{self.left} {self.operator} {self.right}"

class AddExpression(BinaryExpression):
    def __init__(self, left, right):
        super().__init__(left, right, "+") 

    def simplify(self):
        left_simplified = self.left.simplify()
        right_simplified = self.right.simplify()

        if isinstance(left_simplified, Lit) and isinstance(right_simplified, Lit):
            return Lit(left_simplified.value + right_simplified.value)

        return AddExpression(left_simplified, right_simplified)
    
class SubExpression():
    def __init__(self,left:Lit,right:Lit)-> None:
        self.left = left.value
        self.right = right.value

    def toString(self):
        return f"{self.left} - {self.right}"
    
    def simplify(self) -> Lit:
        output = self.left - self.right
        return Lit(output)
  
# i = 1
# l = Lit(i)
# r = Lit(value=20)
# s = l.Sub(r)
# a = l.Add(r)

# print(a.toString())
# print(a.simplify().toString())
# print(s.toString())
# print(s.simplify().toString())
x = Lit(4).Add(Lit(5)).Add(Lit(10))
print(x.simplify())
# print(x.toString())