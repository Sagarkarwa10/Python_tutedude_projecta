dictionary={"sagar":95,"surbhi": 67,"ali":78,"zeeshan":94,"shaan":89}
checkinp=input("enter the students name ")
if checkinp in dictionary:
    print(f"{checkinp}'s  marks",dictionary[checkinp])
else:
    print (f"{checkinp}'s   not present in dictionary")
