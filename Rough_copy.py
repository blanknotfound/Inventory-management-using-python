

'''program to display the stock of laptops in the store
    and reduce or add according to the user input'''
#doc string is needed
#pring(laptop_portal.__doc.__) helps to print the doc string of the function


def laptop_portal():
    """This is for the accessing the laptop.txt file containing in the same folder/file of
the exact program existence"""
    file = open("AAA.txt","r")
    laptop_dictionary={}
    laptop_id = 1
    for line in file:
        line = line.replace("\n","")
        l= line.split(",")
        laptop_dictionary[laptop_id]=1
        laptop_id+= 1
    return laptop_dictionary

laptop_dictionary={}
loop = True

def for_user_input():
    """This is for getting the user input and have different functions according to the need
 of the user"""
    print(laptop_dictionary)
    loop = True
    while loop == True:
        print("Press 1 to sale the laptop to costumer:")
        print("Press 2 to purchase the laptop from consumer:")
        print("Press 3 to exit from the system portal:")
        user_input = int(input("Enter the refered number from the above options : "))

        if user_input ==1:
            name=input("Enter Your Name : ")
            phone_no = input("Enter Your Phone Number: ")

            print("\n")
            print("S/N \t Laptop Name \t Company Name \t Price \t Quantity \t Graphics \t RAM")
            print("\n")

            file = open("laptop.txt","r")
            a=1
            for line in file:
                print(a,"\t"+line.replace(",","\t"))
                a =a+1
            print("-----------------------------------")
            file.close()
            valid_id =int(input("please provide the ID of the laptop you want to book"))
            while valid_id <= 0 or valid_id > len(laptop_dictionary):
                print("please provide a valid laptop id")

                print("\n")
                valid_id =int(input("please provide the ID of the laptop you want to book"))

            user_quantity=int(input("please provide the required quatity"))
            print("\n")

            get_quantity_of_selected_laptop =laptop_dictionary[valid_id][3]
            while user_quantity <= 0 or user_quantity > int(get_quantity_of_selected_laptop):
                print("Dear customer, the quantity looking is not available")
                print("\n")

                user_quantity =int(input("Please provide another quantity requirement:"))
        
            print("\n")
        
        #restocking the text file
            laptop_dictionary[valid_id][3]= int(laptop_dictionary[valid_id][3])-int(user_quantity)

            file =open("laptop_details.txt","w")
            for values in laptop_dictionary.values():
                file.write(str(values[0])+","+str(values[2])+","+str(values[3]))
                file.write("\n")
            file.close()

        elif user_input ==2:
            print("Thank you for purchasing the laptop")
            print("\n")

        elif user_input ==3:
            loop = False
            print("Thank you for using the system ")
            print("\n")

        else:
            print("YOur opion",user_input,"does not seem to match as per our requirement")
            print("\n")
        return user_input
    

