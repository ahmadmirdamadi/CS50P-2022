import re

def main():
    print(convert(input("Enter: ")))

def convert(s):
    isCorrectFormat = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if isCorrectFormat:
        pieces = isCorrectFormat.groups()
        if int(pieces[1]) > 12 or int(pieces[5]) > 12:
            raise ValueError
        avzamin = new_format(pieces[1], pieces[2] , pieces[3])
        sezamin = new_format(pieces[5], pieces[6] , pieces[7])
        return avzamin + ' to ' + sezamin
    else:
        raise ValueError




def new_format(hour, minute, am_pm):
    if am_pm == "PM":
       if int(hour) == 12:
           hour_jadid = 12
       else:
           hour_jadid = int(hour) + 12
    else:
        if int(hour) == 12:
            hour_jadid = 0
        else:
            hour_jadid = int(hour)
    if minute == None:
        minute_jadid = ':00'
        zamin_jadid = f"{hour_jadid:02}" + minute_jadid
    else:
        zamin_jadid = f"{hour_jadid:02}" + ":" + minute


    return zamin_jadid



if __name__ == "__main__":
    main()