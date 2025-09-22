import re
password = input("Enter password:").strip()
score = 0
#check lenght
if len(password)>=8: score+=5
else:
    print("Too short(<8 chars)")
#check uppercase,lowercase,digit,special chars
    if re.search(r"[A-Z]",password): score+=6
else:
    print("missing uppercase")
    if re.search(r"[a-z]",password): score+=6
else:
    print("missing lowercase")
    if re.search(r"\d",password): score+=2
else:
    print("missing digit")
    if re.search(r"\Windows",password): score+=2
else:
    print("missing special chars")
