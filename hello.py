import sys


def default():
    print("Hello!")


def slovak():
    print("Ahoj!")


def french():
    print("Bonjour!")


def main():
    if sys.argv[1] == "sk":
        slovak()
    elif sys.argv[1] == "fr":
        french()
    else:
        default()


if __name__ == "__main__":
    main()
