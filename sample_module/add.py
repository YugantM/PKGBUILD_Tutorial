import click
import sys

@click.command()
def add():
    if len(sys.argv) == 3:
        print(int(sys.argv[1])+int(sys.argv[2]))
        return (int(sys.argv[1])+int(sys.argv[2]))
    else:
        print("ERROR:",str(len(sys.argv)-1)," arguments given instead of 2")
