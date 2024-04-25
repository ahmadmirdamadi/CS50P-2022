import re

def main():
    print(count(input("enter: ")))

def count(s):
    um = re.findall(r"\b\w*um\W", s , re.IGNORECASE)
    return len(um)

if __name__ == "__main__":
    main()