import sys

def add_them_all(filename):
    sum = 0
    ### Your code here


    with open ('info450_fall_2020/week5/homework/a.txt' , 'r') as a, open ('info450_fall_2020/week5/homework/b.txt' , 'r') as b, open ('info450_fall_2020/week5/homework/c.txt' , 'r') as c, open ('info450_fall_2020/week5/homework/d.txt' , 'r') as d, open ('info450_fall_2020/week5/homework/e.txt' , 'r') as e:
        for line in a:
            total_1 = sum + int(line)
            
            
        for line in b:
            total_2 = sum + int(line)
            
            
        for line in c:
            total_3 = sum + int(line)
            
                          
        for line in d:
            total_4 = sum + int(line) 
            
            
        for line in e:
            total_5 = sum + int(line)

        sum = total_1, total_2, total_3, total_4, total_5
            
        
            

    ### End of your code
    return sum

if __name__ == "__main__":
    fname = sys.argv[0]
    print(f"Processing {fname}")
    print(add_them_all(fname))