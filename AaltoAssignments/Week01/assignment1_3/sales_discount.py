def main():
    productPrice = float(input("Enter the price of the product:\n"))
    productNumber = int(input("Enter the number of the products:\n"))
    totalPrice = productPrice * productNumber
    discountPercentage = int(input("Enter the discount percentage:\n")) * 0.01
    discountedProduct = float((productPrice * (1.0 - discountPercentage)))
    discountedProducts = discountedProduct * productNumber
    productsSaving = totalPrice - discountedProducts

    print("Price of the products after discount: ", discountedProducts)
    print("Price of one product after discount: ", discountedProduct)
    print("You saved together ", productsSaving, " euros")

main()
