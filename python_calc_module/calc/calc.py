import sys
import add


if __name__ == "__main__":
    if len(sys.argv) == 4:
        add.add(int(sys.argv[2]),int(sys.argv[3]))
    else:
        print("ERROR:",str(len(sys.argv)-1)," arguments given instead of 3")
