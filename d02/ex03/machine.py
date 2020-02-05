import random
from beverages import *

class CoffeeMachine:
    def __init__(self):
        self.served = 0

    class EmptyCup(HotBeverage):
        price = 0.90
        name = 'empty cup'

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
              Exception.__init__(self, "This coffee machine has to be repaired.")

    def repair(self):
        self.served = 0

    def serve(self, param):
        empty = self.EmptyCup()
        if self.served == 10:
            raise CoffeeMachine.BrokenMachineException()

        if random.randint(1,2) == 2:
            self.served += 1
            print(self.served)
            return param.description()
        else:
            return empty.description()

if __name__ == "__main__":
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuchino = Cappuchino()
    machine = CoffeeMachine()
    for x in range(30):
        try:
            a = machine.serve(coffee)
            print(a)
        except Exception as e:
            print(e)
    print ("End loop")
    machine.repair()
    for x in range(30):
        try:
            a = machine.serve(coffee)
            print(a)
        except Exception as e:
            print(e)


    # print(coffee)
    # print(tea)
    # print(chocolate)
    # print(cappuchino)



