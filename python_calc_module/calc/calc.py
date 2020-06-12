import sys
import add
import mul

def calc(o,a,b):
   if o==0:
      print(add.add(a,b))
      return add.add(a,b)
   if o==1:
      print(mum(a,b))
      return mul(a,b)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        calc(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
    else:
        print("ERROR:",str(len(sys.argv)-1)," arguments given instead of 3")
