from validator_collection import validators

def main():

    post = input("enter: ")
    try:
        pv = validators.email(post)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()