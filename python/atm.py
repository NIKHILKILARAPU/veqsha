print("insert your card")
avail_blalance=8200
correct_pin=int(input("enter your pin: "))
if correct_pin == 1107:
   user_choise=int(input("enter your choise: \n 1-Balance enquiry \n 2-Withdraw \n 3-Fast cash\n enter your choise: "))
   if user_choise == 1:
       print("total available balance: 8200")
   elif user_choise == 2:
      requested_amount=int(input("enter  amount to be withdrawed in multiples of 100: "))
      if requested_amount % 100==0 and requested_amount<=avail_blalance:
         conformation=int(input("Collect your amount \n do you want to display remaining balance \n 1-yes \n 2-no \n  enter your option: "))
         if conformation ==1:
            print(f"Your remain Balance is: {avail_blalance-requested_amount}")
         elif conformation ==2:
            print(f"thankyou vist again")
         else:
            print("please enter a valid option")
      elif requested_amount % 100!=0 and requested_amount<=avail_blalance:
         print("enter amount in multiples of 100")
      elif  requested_amount>avail_blalance:
         print("insufficient balance")
      else:
         print("please enter a valid option")
   elif user_choise == 3:
      fast_cash=int(input("enter your fast cash: \n 1-1000 \n 2-5000 \n 3-10000 \n 4-20000 \n enter your option: "))
      if fast_cash == 1  :
         if 1000<avail_blalance:
          print(f"You sucessfully withdrawed your amount and remaining balance is {avail_blalance-1000}")
         else:
          print("Requested amount is not there in your account")
      elif fast_cash == 2:
         if 5000 < avail_blalance:
            print(f"You sucessfully withdrawed your amount and remaining balance is {avail_blalance - 5000}")
         else:
            print("Requested amount is not there in your account")
      elif fast_cash == 3:
         if 10000 < avail_blalance:
            print(f"You sucessfully withdrawed your amount and remaining balance is {avail_blalance - 10000}")
         else:
            print("Requested amount is not there in your account")
      elif fast_cash == 4:
         if 20000<avail_blalance:
          print(f"You sucessfully withdrawed your amount and remaining balance is {avail_blalance-20000}")
         else:
          print("Requested amonut is not there in your account")
      else:
         print("please enter a valid option")
   else:
      print("please enter a valid option")
else:
    print("incorrect pin")



