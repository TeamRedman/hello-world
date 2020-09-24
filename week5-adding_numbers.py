import sys

def add_them_all(filename):
    sum = 0
    ### Your code here


    with open ('info450_fall_2020/week5/homework/a.txt' , 'r') as a, open ('info450_fall_2020/week5/homework/b.txt' , 'r') as b, open ('info450_fall_2020/week5/homework/c.txt' , 'r') as c, open ('info450_fall_2020/week5/homework/d.txt' , 'r') as d, open ('info450_fall_2020/week5/homework/e.txt' , 'r') as e:
        total_1 = 0
        for line in a:
            total_1 = total_1 + int(line)
            
        total_2 = 0    
        for line in b:
            total_2 = total_2 + int(line)
            
        total_3 = 0    
        for line in c:
            total_3 = total_3 + int(line)
            
        total_4 = 0                  
        for line in d:
            total_4 = total_4 + int(line) 
            
        total_5 = 0    
        for line in e:
            total_5 = total_5 + int(line)

        sum = total_1, total_2, total_3, total_4, total_5
            
        
            

    ### End of your code
    return sum

if __name__ == "__main__":
    fname = sys.argv[0]
    print(f"Processing {fname}")
    print(add_them_all(fname))