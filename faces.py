def convert(f):
    f=f.replace(':)', "🙂").replace(':(', "🙁")
    return f
def value():
    f=input("input")
    f=convert(f)
    print(f)
value()
