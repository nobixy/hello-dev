import argparse


def greet(name):
    return f"Hello, {name}! Welcome to the dev server."


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", nargs="?", default="world")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
