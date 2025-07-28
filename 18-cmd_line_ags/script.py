import argparse

parser = argparse.ArgumentParser(
    description="Provide a positive int, the it will be print",
)

parser.add_argument(
    "-n",
    "--number",  # short and long form
    type=int,  # value must be an int
    help="A positive integer",  # show this in --help
    required=True,  # must be passed
)

args = parser.parse_args()

print(f"You passed: {args.number}")
