"""try:
    x=10/0
except:
    print("Cannot Divide By Zero")
    """
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print(" Invalid input! Not a number.")
finally:
    print(" Program finished.")
