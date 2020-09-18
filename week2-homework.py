import logging
logging.basicConfig(level=logging.DEBUG)
def squared_threes():
    return_value = []
    print([i for i in range(0, 100, 3) if i % 3 == 0 ])
    return return_value
if __name__ == "__main__":
   for x in squared_threes():
       print(x)
       