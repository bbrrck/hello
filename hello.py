import sys

def slovak():
    print("slovak")

def default():
    print("hello")

def main():
    if sys.argv[1] == "sk":
        slovak()
    else:
        default()
    
if __name__ == "__main__":
    main()
