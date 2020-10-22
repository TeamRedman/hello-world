# Step 1. How to get program to spiral in a 2D array
# Step 2. Make functions to move to different coordinates in the array
# Step 3. Create a loop for spiral 



def right(x,y):
    return x+1, y
def down(x,y):
    return x,y-1
def left(x,y):
    return x-1,y
def up(x,y):
    return x,y+1   
def movement():
    for n in moves (go=1):
        if n%2:
            return right
            for i in range (n):
                return down
            for i in range(n):
                return left
        else:
            return left
            for i in range(n):
                return up
            for i in rnage(n):
                return right