def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("How many meow? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

nihao = ["david", "shun","good"]
for i in range(len(nihao)):
    print(i+1,nihao[i])

haha={"david":"nihao",
      "shun":"henhao",
      "nihao":"feichanghao"}
for student in haha:
    print(student,haha[student],sep=", ")

studnets=[
    {"name":"david","house":"shark","patronus":"nihao"},
    {"name":"shun","house":"thunder","patronus":None},
    {"name":"nihao","house":"turtle","patronus":"hehe"}
]

for student in studnets:
    print(student["name"],student["house"],student["patronus"])
