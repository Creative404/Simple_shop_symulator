import time

class shop:
    welcomer = "\nwelcome in Shop what u want to do?:\n"
    choicee = (f'go to one of alles: "dairy", "fruits", "meat"\nor\n'
               f'look at your cart\nor\n'
               f'go to cash register')
    Product_choice ={}
    cart = []

    def __init__(self, alley):
        self.alley = alley


    def items(self):
        for product, price in self.alley.items():
            print(f'{product} : {price}')
            self.Product_choice[product] = price
        return self.Product_choice

    def choice(self):
        self.pre_choice = "what u want to do?:\n"
        self.menu_choice = (f'go to one of alles: "dairy", "fruits", "meat"\nor\n'
              f'look at your cart\nor\n'
              f'go to cash register')
        print(self.pre_choice)
        print(self.menu_choice)

    def add_to_cart(self,Usr_cart):
        self.cart.append(Usr_cart)

    def show_cart(self):
        print()
        print("your cart contans:")
        for Usr_cart in self.cart:
            print(Usr_cart)

    def register(self):
        print()
        print("*scanning products sounds*")
        time.sleep(2)
        print("thanks for buying in our shop")
        time.sleep(0.5)


def User_choice_where():
    print("\npick one:\n"
          f'"dairy", "fruits", "meat"\n'
          f'"cart" \n'
          f'"register"\n')
    while True:
        list_choice = ["dairy", "fruits", "meat", "cart", "register", "cart"]
        User_choice = input("I want to: ").lower()
        if User_choice in list_choice:
            print(User_choice)
            break
        else:
            print("pick something form list\n")
    return User_choice


choice = shop("")
print(shop.welcomer)
print(shop.choicee)
alley_dairy = shop({"milk":"2$","cheese":"3$","yoghurt":"1$",})
alley_meat = shop({"beef":"8$","lamb":"10$","chicken":"5$",})
alley_fruits = shop({"apple":"1$","banana":"2$","orange":"2$",})

while True:
    User_choice = User_choice_where()

    if User_choice == "dairy":
        print(f'Products in "dairy" alley:\n')
        alley_dairy.items()

        print(f'\nWhat u wanna add to your cart? (or type "back")')

        cart_decison = input("pick a product: ").lower()

        if cart_decison in shop.Product_choice:
            alley_dairy.add_to_cart(cart_decison)
            shop.Product_choice = {}

        elif cart_decison == "back":
            print("\n")
            alley_dairy.choice()
        else:
            print("pick valid product")
            shop.Product_choice = {}

    if User_choice == "meat":
        print(f'Products in "meat" alley:\n')
        alley_meat.items()

        print(f'\nWhat u wanna add to your cart? (or type "back")')

        cart_decison = input("pick a product: ").lower()

        if cart_decison in shop.Product_choice:
            alley_meat.add_to_cart(cart_decison)
            shop.Product_choice = {}

        elif cart_decison == "back":
            print("\n")
            alley_meat.choice()
        else:
            print("pick valid product")
            shop.Product_choice = {}

    if User_choice == "fruits":
        print(f'Products in "fruits" alley:\n')
        alley_fruits.items()

        print(f'\nWhat u wanna add to your cart? (or type "back")')

        cart_decison = input("pick a product: ").lower()

        if cart_decison in shop.Product_choice:
            alley_fruits.add_to_cart(cart_decison)
            shop.Product_choice = {}

        elif cart_decison == "back":
            print("\n")
            alley_fruits.choice()
        else:
            print("pick valid product")
            shop.Product_choice = {}

    if User_choice == "cart":
        choice.show_cart()

    if User_choice == "register":
        choice.register()
        time.sleep(0.5)
        break

input("\ntype anything to exit")


