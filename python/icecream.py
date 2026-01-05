ice_creams=["CHOCOLATE(30)-1","VENEELA(30)-2","BUTTER SCOTCH(50)-3","SRABERRY(30)-4","BROWINE(60)-5","MIXED(70)-6"]
hardness=["HARD-1","NORMAL-2","SMOOTH-3"]
ice_rate=[30,30,50,30,60,70]
count=[0,0,0,0,0,0]
payment_method=["CASH-1","UPI-2","DEBIT CARD-3"]
selected_ice=[]
selected_hardness=[]
total=20
rate_index=0
bill_status=False
print("welcome to Autometic IceCream Maker")
print("----------------------------------------------------------------------------------------")
noof_ice=int(input("enter no of ice cream you want: "))
print(f"ICE CREAMS AVAILABLE:{ice_creams} ")
print(f"HARDNES AVAILABLE:{hardness} ")
for i in range(0,noof_ice):
    ice=int(input(f"enter  ice cream you want: "))
    selected_ice.append(ice-1)
    hard=int(input(f"enter hardness of  ice cream you want: "))
    selected_hardness.append(hard-1)
for j in range(0,noof_ice):
    rate_index=selected_ice[j]
    total=total+ice_rate[rate_index]
    count[rate_index]=count[rate_index]+1
payment_option=int(input(f"enter payment option:{payment_method}: "))
if payment_option == 1:
    print(f"please give cash of {total} in reception and collect your ticket")
    payment_option = "CASH"
    bill_status=True
elif payment_option == 2:
    print("please scan above qr and pay amount")
    payment_option = "UPI"
    bill_status=True
elif payment_option == 3:
    card_number = int(input("enter your card number: "))
    cvv_number = int(input("enter your cvv number: "))
    user_name = input("enter your name on card: ")
    if len(str(card_number)) != 16:
        print("invalid card number")
    elif len(str(cvv_number)) != 3:
        print("invalid cvv number")
    else:
        payment_option = "DEBIT CARD"
        bill_status=True
else:
    print("invalid payment method")
if bill_status==True:
    print("your bill")
    print("__________________________________________________________________________________")
    print(f"TOTAL ICE CREAMS SELECTED:{noof_ice} ")
    print(f"CHOCOLATE(30):{count[0]} ")
    print(f"VENEELA(30):{count[1]} ")
    print(f"BUTTER SCOTCH(50):{count[2]} ")
    print(f"STRABERRY(30):{count[3]} ")
    print(f"BROWNIE(60):{count[4]} ")
    print(f"MIXED(70):{count[5]} ")
    print("SERVICE TAX: 20")
    print(f"PAYMENT TYPE:{payment_option}")
    print(f"TOTAL:{total} ")
    print(f"THANK YOU VIST AGAIN ")
    print("_________________________________________________________________________________")
else:
    print("PAYMET FAILED")




