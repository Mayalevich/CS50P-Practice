fruit={
    "apple":"130",
    "avocado":"50",
    "banana":"110",
    "cantaloupe":"50",
    "grapfruit":"60",
    "grapes":"90",
    "honeydewmelon":"50",
    "kiwifruit":"90",
    "lemon":"15",
    "lime":"20",
    "nectarin":"60",
    "orange":"80",
    "peach":"60",
    "pear":"100",
    "pineapple":"50",
    "plums":"70",
    "strawberries":"100",
    "sweetcherries":"100",
    "tangerine":"50",
    "watermelon":"80",
}
f=input("Fruit?")
for i in fruit:
    if i == f.lower().replace(" ",""):
        print("calories: ", fruit[i])
