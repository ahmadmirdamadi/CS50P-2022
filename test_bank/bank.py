def main():
    greeting = input("enter: ")
    meghdar = value(greeting)
    print(f"${meghdar}")
    

def value(greeting):
    greeting = greeting.lower().strip()
    if "hello" in greeting:
        return 0
    elif "h" == greeting[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()