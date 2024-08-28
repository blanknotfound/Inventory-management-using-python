
#read.py file
file = open("Purchase.txt","r")
laptop_list =[]

for line in file:
    line = line.replace("\n","")
    l= line.split(",")
    laptop_list.append(l)

#print(laptop_list)

loop= True
while loop == True:
    print("\t \t  Welcome TO The Online Portal Of ABC Laptop Shop")
    print("Press 1 to Purchase the laptop from the consumer: ")
    print("Press 2 to sale the laptop to the costumer: ")
    print("Press 3 to exit the system portal: ")

    user_input_num= int(input("Enter the sutaible number as of your need: "))
    print("\n")

    while user_input_num == 1:
        
        emp_name =input("Enter the emloyee name : ")

        print("\n")
        print("---------------------------------------------------------------------------------------------")
        print("|S.N.|Laptop Name\t | Company name  |Price \t | Quant | Graphics \t | RAM \t")
        print("---------------------------------------------------------------------------------------------")
        file = open("Purchase.txt","r")
        a=1
        for line in file:
            print("|",a," |"+line.replace(",","\t | "))
            a += 1
            print("---------------------------------------------------------------------------------------------")
        print("\n")
        print("\t**----------------------------*Products Above*--------------------------------------**")
        print("\n")
        file.close()

        purchase_ID= int(input("Enter the desired Id of product to be added in the store: "))
        while purchase_ID > len(laptop_list) or purchase_ID <=0 :
            print("The above deal cannot be carried. Please provide the ID from the above")
            purchase_ID= int(input("Enter the desired Id of product to be added in the store: "))
            print("\n")

        purchasing_num=int(input("Enter the required number of laptops : "))
        while purchasing_num <=0:
            print("Please provide the quantity needed to be add in the store: ")
            purchasing_num=int(input("Enter the required number of laptops : "))
            print("\n")

            #restocking the text file
            
            laptop_list[purchase_ID-1][3]= int(laptop_list[purchase_ID-1][3])+int(purchasing_num)
            
            print(laptop_list)

            again_purchase=input("Would you like to add more of laptops to the store(Y/N)?: ").upper()
            while again_purchase!= "Y" or again_purchase!= "N":
                again_purchase=input("Please type y for yes and n for no(Y/N)?: ").upper()

            if again_purchase=="Y":
                user_input_purchase= 1


    while user_input_num ==2:
        name= input("enter your name: ")
        phone_number=int(input("enter your phone number: "))

        print("\n")
        print("---------------------------------------------------------------------------------------------")
        print("|S.N.|Laptop Name\t | Company name  |Price \t | Quant | Processor \t | Graphics \t")
        print("---------------------------------------------------------------------------------------------")
        file = open("Purchase.txt","r")
        a=1
        for line in file:
            print("|",a," |"+line.replace(",","\t | "))
            a += 1
            print("---------------------------------------------------------------------------------------------")
        print("\n")
        print("\t**---------------------------*Products Above*---------------------------------**")
        print("\n")
        file.close()

        valid_id =int(input("please provide the ID of the laptop you want to book"))
        while valid_id <= 0 or valid_id > len(laptop_list):
            print("please provide a valid laptop id")

            print("\n")
            valid_id =int(input("please provide the ID of the laptop you want to book"))

        user_quantity=int(input("please provide the required quatity"))
        print("\n")

        get_quantity_of_selected_laptop =laptop_list[valid_id][3]
        while user_quantity <= 0 or user_quantity > int(get_quantity_of_selected_laptop):
            print("Dear customer, the quantity looking is not available")
            print("\n")

            user_quantity =int(input("Please provide another quantity requirement:"))
        
        print("\n")
        
        #restocking the text file
        laptop_list[valid_id][3]=int(laptop_list[valid_id][3])-int(user_quantity)

        """

        #write.py file 
        file =open("laptop_detaileds.txt","w")
        for values in laptop_dic.values():
            file.write(str(values[0])+","+str(values[2])+","+str(values[3]))
            file.write("\n")
        file.close()"""

    while user_input_num==3:
        loop = False
