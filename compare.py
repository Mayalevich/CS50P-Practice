i=0



while i<1:
    try:
        x=float(input("what is the your average?"))
        if 90<=x<=100:
            print("Grade:A")
            i=i+1
        elif x<0 or x>100:
            print("Invalid average")
        elif x>=80:
            print("Grade:B")
            i=i+1
        elif x>=70:
            print("Grade:C")
            i=i+1
        elif x>=60:
            print("Grade:D")
            i=i+1
        else:
            print("Grade:F")
    except ValueError:
        print("Invalid input")
