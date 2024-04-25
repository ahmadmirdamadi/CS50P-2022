def main():
    fraction = input("enter: ")
    fc = convert(fraction)
    khoroji = gauge(fc)
    print(khoroji)



def convert(fraction):
    while True:
        try:
            adad , den = fraction.split("/")
            adad_jadid = int(adad)
            den_jadid = int(den)

            f = adad_jadid / den_jadid

            if f<=1:
                return int(fraction * 100)
            else:
                f = input("enter: ")
                pass



        except (ValueError,ZeroDivisionError):
                raise


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return str(percentage) + '%'



if __name__ == "__main__":
    main()