class ShoppingCart:
    
    def __init__(attr):
        attr.items = []
    
    def addItem(attr,name:str,qty:int,price:float):
        attr.items.append({
            name:name,
            qty:qty,
            price:price
        })
    
    def removeItem(attr,name:str):
        for item in attr.items:
            if item[0] == name:
                attr.items.remove(item)
                break

    # def numbers(*num:int,**kaargs):
    #   return num

    def calculateTotal(attr) -> float:
        total = 0

        for name,qty,price in attr.items:
            total += (qty * price)
        
        return total
    
    def summary(attr):
        print("Cart content\n")

        for name, qty, price in attr.items:
            print(f"{name}: {qty} @ Ksh {price}")
        print(f"\nTotal: Ksh. {attr.calculateTotal():.2f}")


if __name__ == "__main__":
    cart:ShoppingCart = ShoppingCart()
    cart.addItem("Mangoes",10,20)
    cart.addItem("Guava",86,10)
    cart.addItem("Apples",1200,10)

    cart.summary()

    print("\n>>> Ordinary Cart <<<\n")
    cart.summary()