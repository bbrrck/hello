import sys

def slovak():
    """Greet user in Slovak."""
    print("ahoj")

def default():
    print("hello")

def main():
    if sys.argv[1] == "sk":
        slovak()
    else:
        default()
    
if __name__ == "__main__":
    main()
