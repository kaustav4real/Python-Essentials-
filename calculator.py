continue_calculate=True
def add(n1,n2):
  return n1+n2
  
def subtract(n1,n2):
  return n1-n2
  
def mulitply(n1,n2):
  return n1*n2
  
def divide(n1,n2):
  return n1/n2

operations={
  "+":add,
  "-":subtract,
  "*":mulitply,
  "/":divide
}

def calculate():
  should_continue=True
  n1=float(input("Enter the first number: "))
  
  for symbol in operations:
    print(symbol)

  while should_continue:
    operation_to_perform=input("Select an operation: ")
    n2=float(input("Enter the second number: "))
    fun=operations[operation_to_perform]
    result=fun(n1,n2)
    print(result)

    choice=input("Press 'y' to continue the calculation. Else press 'n' to start a new calculation")
    if choice=='y':
      n1=result
    else:
      calculate()

calculate()
  
  
