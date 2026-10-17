import sys

from sayings import hello, goodbye

args = sys.argv

if len(args) < 2:
    sys.exit("Too little cortisol")

if args[1] == "hello":
    hello(args[2])
elif args[1] == "goodbye":
    goodbye(args[2])
else:
    print(args[1])


print(__name__)