import sys


def default():
    print("Hello")


def slovak():
    print("Ahoj")


def main():
    if sys.argv[1] == "sk":
        slovak()
    else:
        default()


if __name__ == "__main__":
    main()