m = [
 "January",
 "February",
 "March",
 "April",
 "May",
 "June",
 "July",
 "August",
 "September",
 "October",
 "November",
 "December"
]

while True:
    date = input("tarikh: ")
    try:
        m,d,y = date.split('/')
        if (int(m) >= 1 and int(m) <= 12)   and  (int(d) >= 1 and int(d) <=31):
            break

    except:
        try:
            m_gadimi , d_gadimi , y = date.split(' ')
            for i  in range(len(m)):
                if m_gadimi == m[1]:
                    m = i+1
            d = d_gadimi.replace(",", "")

            if (int(m) >= 1 and int(m) <= 12)    and    (int(d) >= 1 and int(d) <=31):
                break

        except:
            print()
            pass

print(f"{y}-{int(m):02}-{int(d):02}")