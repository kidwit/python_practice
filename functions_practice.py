hello = "Hello User!"

print (hello)


pack = ["Marlboro", "NewPort","Camel"]

print(pack)

def eat_lunch(lunch_items):
    if not lunch_items:
        print("My lunchbox is empty!")
    else:
        for i, item in enumerate(lunch_items):
            if i == 0:
                print(f"First I eat {item}")
            else:
                print(f"Next I eat {item}")
                print("Example 1:")
eat_lunch(["sandwich", "apple", "cookie"])