alpha="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
invalid=" ,!?."
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
   if len(s)<2 or len(s)>6:
       return False
   if s[0] not in alpha or s[1] not in alpha:
       return False
   for char in s:
        if char in invalid:
            return False
   for i in range(len(s)):
        if s[i].isdigit():
            #if s[3]=="0" and len(s)==4:
                #return True
            if s[i] == '0' and i-len(s)+1!=0:
                return False
   else:
       return True

main()
