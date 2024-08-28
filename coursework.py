

import datetime


file=open("laptop.txt","r")
laptop_dictionary ={}
laptop_id=1
for line in file:
    line = line.replace("\n","")
    l= line.split(",")
    laptop_dictionary[laptop_id]=l
    laptop_id+= 1

#print(laptop_dictionary)

loop = True

while loop == True:
    print("Press 1 to sale the laptop to costumer:")
    print("Press 2 to purchase the laptop from consumer:")
    print("Press 3 to exit from the system portal:")

    user_input= int(input("enter the refered number:" ))
    print("\n")

    if user_input ==1:
        name= input("enter your name: ")
        phone_number=int(input("enter your phone number: "))

        print("S.N. \t laptop name \t company name \t price \tquantity   graphics \t RAM")
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
        print(laptop_dictionary)
        file =open("laptop_details.txt","w")
        for values in laptop_dictionary.values():
            file.write(str(values[0])+","+str(values[2])+","+str(values[3]))
            file.write("\n")
        file.close()

        #getting user purchase items
        name_of_product= laptop_dictionary[valid_id][0]
        quantity_selected_by_user= user_quantity
        unit_price =laptop_dictionary[valid_id][2]
        price_of_selected_item= laptop_dictionary[valid_id][2].replace("$","")
        total_price = int(price_of_selected_item)*int(quantity_selected_by_user)
        
        #creating the list to store the purchase details
        user_purchased_laptops=[]
        user_purchased_laptops.append([name_of_product,quantity_selected_by_user,unit_price,total_price])

        shipping_cost= input("do you want to ship your product? (Y/N) ").upper()

        if shipping_cost =="Y":
            total=0
            shipping_cost = 400
            for i in user_purchased_laptops:
                total += int(i[3])
            grand_total = total + shipping_cost
            #today_date_and_time = datetime.now() # type: ignore
            print("\n")
            print("\t laptop shop bill")
            print("\n")
            print("\t kamalpokhari kathmandu|phone no:7585858")
            print("\n")
            print("------------------------------")
            print("Laptop details are:")
            print("------------------------------")
            print("Name of the costumer:"+str(name))
            print("Contact number: "+str(phone_number))
            #print("Date and time of purchase"+str(today_date_and_time))
            print("------------------------------")
            print("\n")
            print("Purchase details are:")
            print("------------------------------")
            print("Item name \t total quantity \t unit price \t total")
            print("------------------------------")

            for i in user_purchased_laptops:
                print(i[0],"\t",i[1],"\t",i[2],"\t",i[3])
            print("------------------------------")
            if shipping_cost:
                print("your shipping cost: ",shipping_cost)
                print("Grand total: $"+str(grand_total))
                print("Note: shipping cost is addid to the grand total")
            else:
                print("Grand total :$"+str(grand_total))
            print("\n")
        else:
            print("NO")
        
        print("\n")
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

    
