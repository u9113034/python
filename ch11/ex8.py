# ch11_24.py
def make_pizza(pizza_size, *toppings):
    # 列出製作pizza
    print("這個 ", pizza_size, " 吋PIZZA所加配料如下")
    for topping in toppings:
        print("--- ", topping)

make_pizza(8, '起司')
make_pizza(12, '鮑魚', '德國香腸', '火腿')

