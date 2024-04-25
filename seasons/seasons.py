from datetime import date
import sys
import re
import inflect

p = inflect.engine()

def main():
    birth_date = input("Date of Birth: ")

    try:
        year, month, day = check_birthday(birth_date)

    except:
        sys.exit("Invalid Date")

    tar = date(int(year) , int(month) , int(day))
    tad = date.today()
    hh = tad - tar
    tt = hh.days * 24 * 60
    khoroj = p.number_to_words(tt, andword="")
    print(khoroj.capitalize() + " minutes")

def check_birthday(birth_date):
    if re.search("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year,month,day = birth_date.split("-")
        return year,month,day

if __name__ == "__main__":
    main()