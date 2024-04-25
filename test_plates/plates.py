def main():
 vorodi = input("enter: ")
 if is_valid(vorodi):
     print("Valid")
 else:
     print("Invalid")



def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    a = 1
    while a < len(s):
        if s[a].isalpha() == False:
            if s[a] == "0":
                return False
            else:
                break
        a += 1


        for a in range(len(s)):
            if s[a].isdigit():
                if not s[a:].isdigit():
                    return False

        for c in s:
            if c in ["." , " " , "!" , "?"]:
                return False





if __name__ == "__main__":
 main()