import sys
import csv

def main():

    check_command_line_arg()
    output = []

    try:

        with open(sys.argv[1], "r") as csvfile:
            khandani = csv.DictReader(csvfile)
            for row in khandani:
                sn = row["name"].split(",")
                output.append({"first": sn[1].lstrip(), "last": sn[0] , "house": row["house"]})


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        nevis = csv.DictWriter(file, fieldnames =["first" , "last" , "house"])
        nevis.writerow({"first": "first" , "last": "last" , "house": "house"})
        for out in output:
            nevis.writerow({"first":out["first"], "last":out["last"], "house":out["house"]})

def check_command_line_arg():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()