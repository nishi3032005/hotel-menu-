menu={
    "pizza":60,
    "pasta":70,
    "coffee":50,
    "burger":70,
    "salad":50,
}
print("welcome to python resturant")
print("pizza:60\npasta:70\ncoffe:50\nburger:70\nsalad:50\n")

order_total = 0

item_1 = input("enter name of item you want to order : ")
if item_1 in menu :
    order_total += menu[item_1]
    print(f"your {item_1} has been added to order")

else:
    print(f"your item {item_1} is not avalaible yet!")

another_order = input("If u want to add another item ? yes/no : ") 

if another_order == "yes":
    item_2=input("enter name of another item : ")
    if item_2 in menu :
        order_total += menu[item_2]
        print(f"item {item_2 }has been added to order ")
    else:
        print(f"item{item_2} is not avaliable yet!")   

print(f"the total amount to items to pay is {order_total}")        

         