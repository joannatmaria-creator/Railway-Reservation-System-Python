class railwayms():
    def __init__(self):
        self.file="rail.txt"
    def book_ticket(self):
        passen_id=input("enter passenger id:")
        passen_name=input("enter passenger name:")
        train_no=input("enter train nuumber:")
        seat_no=input("enter seat number:")
        desti=input("enter destination:")
        try:
            with open(self.file,"r") as f:
                railways=f.readlines()
        except:
            railways=[]
        for railway in railways:
            if railway.strip()=="":
                continue
            i,n,t,s,d=railway.strip().split(",")
            if i==passen_id:
                print("ALREADY ADDED")
                return
            if s==seat_no:
                print("SEAT ALREADY BOOKED")
                return
        with open(self.file,"a") as f:
            f.write(str(passen_id)+","+passen_name+","+str(train_no)+","+str(seat_no)+","+desti+"\n")
        print("BOOKED TICKET")
    def view_ticket(self):
        with open(self.file,"r") as f:
            railways=f.readlines()
        if not railways:
            print("NO TICKETS TO VIEW")
            return
        print("TICKETS LIST")
        for railway in railways:
            if railway.strip()=="":
                continue
            i,n,t,s,d=railway.strip().split(",")
            print("\npassenger id:",i,
                  "\npassenger name:",n,
                  "\ntrain number:",t,
                  "\nseat number:",s,
                  "\ndestination:",d,"\n")
    def search_ticket(self):
        passen_id=input("enter passenger id:")
        with open(self.file,"r") as f:
            railways=f.readlines()
        found=False
        for railway in railways:
            if railway.strip()=="":
                continue
            i,n,t,s,d=railway.strip().split(",")
            if i==passen_id:
                print("\npassenger id:",i,
                      "\npassenger name:",n,
                      "\ntrain number:",t,
                      "\nseat number:",s,
                      "\ndestination:",d,"\n")
                found=True
        if not found:
            print("INVALID ID")
    def update_ticket(self):
        passen_id=input("enter passenger id:")
        passeng_name=input("enter passenger name:")
        trains_no=input("enter train nuumber:")
        seats_no=input("enter seat number:")
        destin=input("enter destination:")
        with open(self.file,"r") as f:
            railways=f.readlines()
        update=[]
        found=False
        for railway in railways:
            if railway.strip()=="":
                continue
            i,n,t,s,d=railway.strip().split(",")
            if i==passen_id:
                update.append(str(i)+","+passeng_name+","+str(trains_no)+","+str(seats_no)+","+destin+"\n")
                found=True
            else:
                update.append(railway)
        with open(self.file,"w") as f:
            f.writelines(update)
        if found:
            print("TICKETS UPDATED")
        else:
            print("INVALID ID")
    def cancel_ticket(self):
        passen_id=input("enter passenger id:")
        with open(self.file,"r") as f:
            railways=f.readlines()
        cancel=[]
        found=False
        for railway in railways:
            if railway.strip()=="":
                continue
            i,n,t,s,d=railway.strip().split(",")
            if i==passen_id:
                found=True
            else:
                cancel.append(railway)
        with open(self.file,"w") as f:
            f.writelines(cancel)
        if found:
            print("CANCELLED TICKET")
        else:
            print("INVALID ID")
system=railwayms()
while True:
    print("\n RAILWAY RESERVATION SYSTEM")
    print("1.book ticket")
    print("2.view ticket")
    print("3.search ticket")
    print("4.update ticket")
    print("5.cancel ticket")
    print("6.EXIT")
    choice=input("enter your choice:")
    if choice=="1":
        system.book_ticket()
    elif choice=="2":
        system.view_ticket()
    elif choice=="3":
        system.search_ticket()
    elif choice=="4":
        system.update_ticket()
    elif choice=="5":
        system.cancel_ticket()
    
    elif choice=="6":
        print("------------EXITING RAILWAY RESERVATION SYSTEM------------------")
        break
    else :
        print("invalid choice :(")
            
        

            

        
            






            



            
            





        
        
                
            
        







    
            
