import sys

def french():
    """Greet user in French."""
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
