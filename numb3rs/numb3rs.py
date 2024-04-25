import re

def main():

    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        ln = ip.split(".")
        for l in ln:
            if int(l) < 0 or int(l) > 255:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()