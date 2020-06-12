import sys
import add

def calc(o,a,b):
   if o==0:
      print(add(a,b))
      return add(a,b)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        return calc(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
    else:
        print("ERROR:",str(len(sys.argv)-1)," arguments given instead of 3")
