import sys

def french():
    print("bonjour")

def default():
    print("hello")

def main():
    if sys.argv[1] == "fr":
        french()
    else:
        default()
    
if __name__ == "__main__":
    main()
