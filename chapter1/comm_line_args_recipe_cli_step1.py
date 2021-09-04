import argparse

"""
Calling the script with the extra parameters works as expected:
$ python comm_line_args_recipe_cli_step1.py 4
"""


def main(number):
    print("#" * number)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int, help="A number")
    args = parser.parse_args()

    main(args.number)
