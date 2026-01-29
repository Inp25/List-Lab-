# List Lab Starter
# Students: fill in code for Series 1–4 below

def series1():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print("Series 1:", fruits)

    new_fruit = input("Name another fruit (capitalize): ")
    fruits.append(new_fruit)
    print("Updated list:", fruits)

    num = int(input("Enter a number to see the corresponding fruit (1-based): "))
    if 1 <= num <= len(fruits):
        print(f"Fruit #{num} is:", fruits[num - 1])
    else:
        print("That number is out of range!")

    fruits = ["Mango"] + fruits
    print("Updated list:", fruits)

    fruits.insert(0, "Bigger Mango")
    print ("New List:", fruits)
    
    print("Fruits that begin with 'P':")
    for fruit in fruits:
        if fruit.startswith('P'):
            print(fruit)


def series2():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print("Series 2:", fruits)

    # Remove the last fruit
    fruits.pop()
    print("After removing last fruit:", fruits)

    # Ask user for a fruit to delete
    fruit_to_delete = input("Which fruit should I delete? ")

    if fruit_to_delete in fruits:
        fruits.remove(fruit_to_delete)
    print("After deletion:", fruits)

    # Bonus
    fruits *= 2
    print("Doubled list:", fruits)

    while True:
        delete_again = input("Delete another fruit (must exist): ")
        if delete_again in fruits:
            while delete_again in fruits:
                fruits.remove(delete_again)
            break
        else:
            print("That fruit is not in the list, try again.")

    print("After removing all occurrences:", fruits)
    
def series3():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    final_list = []

    for fruit in fruits:
        while True:
            answer = input(f"Do you like {fruit.lower()}? (yes/no) ").lower()
            if answer == "yes":
                final_list.append(fruit)
                break
            elif answer == "no":
                break
            else:
                print("Please answer 'yes' or 'no'.")

    print("Fruits you like:", final_list)

def series4():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]

    reversed_fruits = [fruit[::-1] for fruit in fruits]

    fruits.pop()  # remove last

    print("Original list after removing last:", fruits)
    print("Reversed list:", reversed_fruits)


def main():
    series1()
    series2()
    series3()
    series4()
