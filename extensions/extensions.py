t = input("enter format: ")
t = t.strip()

if  t.endswith(".gif"):
    print("image/gif")

elif t.endswith(".jpg") or t.endswith(".jpeg"):
    print("image/jpeg")

elif t.endswith(".png"):
    print("image/png")

elif t.endswith(".pdf"):
    print("application/pdf")

elif t.endswith(".txt"):
    print("text/plain")

elif t.endswith(".zip"):
    print("application/zip")

elif t.endswith(".txt.pdf"):
    print("application/pdf")

elif t.endswith(".PDF"):
    print("application/pdf")

elif t.endswith(" .PDF "):
    print("application/pdf")
else:
    print("application/octet-stream")
