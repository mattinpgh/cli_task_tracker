"""
Use this file to test concepts before trying to implement them in the code and
breaking things.
"""
import argparse

parser = argparse.ArgumentParser(prog="wahoo", description="squarin' a number, yeein the haws")
group = parser.add_mutually_exclusive_group()

group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")

args = parser.parse_args()

answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")
