import argparse


def main(number, other_number):
    result = number * other_number
    print(f"The result is: {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n1", type=int, default=1, help="A number")
    parser.add_argument("-n2", type=int, default=1, help="Another number")

    args = parser.parse_args()

    main(args.n1, args.n2)
