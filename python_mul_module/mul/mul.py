import sys

def mul(x,y):
    print(x*y)
    return x*y
    

if __name__ == "__main__":
    if len(sys.argv) == 3:
        add(int(sys.argv[1]),int(sys.argv[2]))
    else:
        print("ERROR:",str(len(sys.argv)-1)," arguments given instead of 2")
