print("welcome come to INDIAN RAILWAYS")
print("---------------------------------------------------------------------------------")
departure_stations=["ELR-1","KKD-2","VIZ-3","BZA-4"]
final_stations=["ELR-1","KKD-2","VIZ-3","BZA-4"]
seat_type=["GEN -1","SLR -2","TIRE_3 -3","TIRE-4 -4"]
payment_method=["CASH-1","UPI-2","DEBIT CARD-3"]
print("select departure station")
print(departure_stations)
departure_option=int(input("enter departure station: "))
print("select final station")
print(final_stations)
final_option=int(input("enter final station: "))
distance=int(input("enter distance: "))
print("select seat type")
print(seat_type)
seat_option=int(input("enter seat type: "))
service_tax=20
ticket_generation=False
seat_charges=0
payment_option=""
total=0
if departure_option<= len(departure_stations):
    if final_option<=len(final_stations):
        if seat_option<=len(seat_type):
            if seat_option==1:
                total = (2 * distance) + service_tax +0
                print("select payment method: ")
                print(payment_method)
                payment_option = int(input("enter payment method: "))
                if payment_option == 1:
                    print(f"please give cash of {total} in reception and collect your ticket")
                    ticket_generation = True
                    seat_charges = 0
                    payment_option = "CASH"

                elif payment_option == 2:
                    ticket_generation = True
                    seat_charges = 0
                    payment_option = "UPI"

                elif payment_option == 3:
                    card_number = int(input("enter your card number: "))
                    cvv_number = int(input("enter your cvv number: "))
                    user_name = input("enter your name on card: ")
                    if len(str(card_number)) != 16:
                        print("invalid card number")
                    elif len(str(cvv_number)) != 3:
                        print("invalid cvv number")
                    else:
                        ticket_generation = True
                        seat_charges = 0
                        payment_option = "DEBIT CARD"
                else:
                    print("invalid payment method")
            elif seat_option == 2:
                total = (2 * distance) + service_tax + 100
                print("select payment method: ")
                print(payment_method)
                payment_option = int(input("enter payment method: "))
                if payment_option == 1:
                    print(f"please give cash of {total} in reception and collect your ticket")
                    ticket_generation = True
                    seat_charges = 100
                    payment_option = "CASH"

                elif payment_option == 2:
                    print(f"please scan the above qr and collect your ticket")
                    ticket_generation = True
                    seat_charges = 100
                    payment_option = "UPI"

                elif payment_option == 3:
                    card_number = int(input("enter your card number: "))
                    cvv_number = int(input("enter your cvv number: "))
                    user_name = input("enter your name on card: ")
                    if len(str(card_number)) != 16:
                        print("invalid card number")
                    elif len(str(cvv_number)) != 3:
                        print("invalid cvv number")
                    else:
                        ticket_generation = True
                        seat_charges = 100
                        payment_option = "DEBIT CARD"
                else:
                    print("invalid payment method")
            elif seat_option == 3:
                total = (2 * distance) + service_tax +200
                print("select payment method: ")
                print(payment_method)
                payment_option = int(input("enter payment method: "))
                if payment_option == 1:
                    print(f"please give cash of {total} in reception and collect your ticket")
                    ticket_generation = True
                    seat_charges = 200
                    payment_option = "CASH"

                elif payment_option == 2:
                    print(f"please scan the above qr and collect your ticket")
                    ticket_generation = True
                    seat_charges = 200
                    payment_option = "UPI"

                elif payment_option == 3:
                    card_number = int(input("enter your card number: "))
                    cvv_number = int(input("enter your cvv number: "))
                    user_name = input("enter your name on card: ")
                    if len(str(card_number)) != 16:
                        print("invalid card number")
                    elif len(str(cvv_number)) != 3:
                        print("invalid cvv number")
                    else:
                        ticket_generation = True
                        seat_charges = 200
                        payment_option = "DEBIT CARD"
                else:
                    print("invalid payment method")
            else:
                total = (2 * distance) + service_tax + 300
                print("select payment method: ")
                print(payment_method)
                payment_option = int(input("enter payment method: "))
                if payment_option == 1:
                    print(f"please give cash of {total} in reception and collect your ticket")
                    ticket_generation = True
                    seat_charges = 0
                    payment_option = "CASH"

                elif payment_option == 2:
                    print(f"please scan the above qr and collect your ticket")
                    ticket_generation = True
                    seat_charges = 300
                    payment_option = "UPI"

                elif payment_option == 3:
                    card_number = int(input("enter your card number: "))
                    cvv_number = int(input("enter your cvv number: "))
                    user_name = input("enter your name on card: ")
                    if len(str(card_number)) != 16:
                        print("invalid card number")
                    elif len(str(cvv_number)) != 3:
                        print("invalid cvv number")
                    else:
                        ticket_generation = True
                        seat_charges = 300
                        payment_option = "DEBIT CARD"
                else:
                    print("invalid payment method")
        else:
            print("invalid seat seletion option")
    else:
        print("invalid final station seletion option")
else:
    print("invalid departure station seletion option")
if ticket_generation==True:
  print("your ticket")
  print("-------------------------------------------------------------------------")
  print(f"DEPARTURE STATION: {departure_stations[departure_option - 1]}")
  print(f"FINAL STATION: {final_stations[final_option - 1]}")
  print(f"DISTANCE: {distance}")
  print(f"SEAT TYPE:{seat_type[seat_option - 1]}")
  print(f"SEAT CHARGES:{seat_charges}")
  print(f"PAYMENT METHOD:{payment_option}")
  print("COST PER KM: 2 RUPEES")
  print(f"SERVICE TAX: {service_tax}")
  print(f"TOTAL: {total}")
else:
  print("ticket generation failed")



