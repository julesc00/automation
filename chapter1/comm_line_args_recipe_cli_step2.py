"""
Change the script to accept an optional argument for the character to print.
The default will be "#". The recipe_cli_step2.py script will look like this:
"""
import argparse


def main(character, number):
    print(character * number)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int, help="A number")
    parser.add_argument("-c", type=str, help="Character to print", default="#")
    args = parser.parse_args()
    main(args.c, args.number)
