import sys

def add_them_all(info450_fall_2020):
    sum = 0
    ### Your code here
    with open ('info450_fall_2020/week5/homework/a.txt' , 'r') as f:
        for line in f:
            sum = sum + int(line)

    ### End of your code
    return sum

if __name__ == "__main__":
    fname = sys.argv[1:119]
    print(f"Processing {fname}")
    print(add_them_all(fname))