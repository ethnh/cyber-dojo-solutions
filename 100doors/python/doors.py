'''The starting files are unrelated to the exercise.

They show examples of writing and testing
  o) a global function
  o) an instance method
Pick the style most suitable to your exercise.
'''

'''
100 doors in a row are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it).
The second time you only visit every 2nd door (door #2, #4, #6, ...).
The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?

[Source http://rosettacode.org]
'''

class Door:    
    def __init__(self, *args, **kwargs):
        self.open = False
    
    def visit(self):
        self.open = not self.open
    
    def is_open(self):
        if self.open: return 'Open!'
        return 'Closed :('
        

def gen_doors(): 
    return [Door() for i in range(100)]


def visit_doors(doors, visit_count):
    for (i, door) in enumerate(doors):
        if (i+1) % visit_count == 0:
            door.visit()
            

def visit_one_hundred_doors():
    doors = gen_doors()
    for i in range(100):
        visit_doors(doors, i+1)
    print([door.is_open() for door in doors])
    return doors
