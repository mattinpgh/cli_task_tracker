import argparse

parser = argparse.ArgumentParser()

parser.add_argument("task", action="store")
args = parser.parse_args()

print(f'The task you\'ve selected is {args.task}')