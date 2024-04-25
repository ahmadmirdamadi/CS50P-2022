import csv
import sys

def main():
    check_correct_args()
    data=[]
    try:
        with open(sys.argv[1]) as csvfile:
            khandan = csv.DictReader(csvfile)
            for khan in khandan:
                data.append(khan)
    except FileNotFoundError:
        sys.exit("Could't read CSV file")

    khoroj = []
    for khan in data:
       house = select_house(khan["characteristic"])
       grade = select_grade(khan["birthdate"])
       khoroj.append({"name": khan["name"], "house": house, "grade": grade})

    with open(sys.argv[2], "w") as file:
        nevis = csv.DictWriter(file, fieldnames=["name" , "house", "grade"])
        nevis.writerow({"name":"name", "house":"house", "grade":"grade"})
        for khan in khoroj:
            nevis.writerow({"name": khan["name"], "house": khan["house"], "grade": khan["grade"]})



def check_correct_args():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not CSV files")


def select_house(char):

    if char in ["courage" , "loyalty" , "adventure"]:
        return "Gryffindor"
    elif char in ["dedication" , "patience" , "honesty"]:
        return "Hufflepuff"
    elif char in ["wisdom" , "creativity" , "perfectionism"]:
        return "Ravenclaw"
    elif char in ["ambition" , "competitive" , "leadership"]:
        return "Slytherin"
    else:
        return "No House"



def select_grade(year):

    age = 2022 - int(year)
    grade = age - 5
    return "Grade " + str(grade)



if __name__ == "__main__":
    main()