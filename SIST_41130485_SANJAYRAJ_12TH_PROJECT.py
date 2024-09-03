print("******************* Welcome To bus Tracker Program********************")
print(" do you want search between distric or area")
pla=input("if city enter 'city' or do u want to search area enter 'area':")
if pla=="area" or pla=="AREA":
    print("please enter the city")
    def chennai():
        print("select your area \n\t1.tnagar=11 \n\t2.anna nagar=12 \n\t3.kk nagar=13")
        while True:
            A1=int(input("enter the codes as per the area you required:"))
            print("      bus no      starting point            ending point")
            if A1==11:
               print("        49C          tnagar                kk nagar")
               print("        13A          tnagar            chennai central    ")
               break
            elif A1==12:
                print("        11A         anna nagar             kk nagar")
                print("        101C        anna nagar               tnagar")
                break
            elif A1==13:
                print("        49C          kk nagar                tnagar")
                print("        11A          kk nagar               anna nagar")
                break
            else:
                print("invalid code")
        print("do you want to continue same city chennai")
        while True:
            a=input("if yes enter 'y' or no enter 'n':") 
            if a=="y" or a=="Y":
                chennai()
                break
            elif a=="n" or a=="N":
                print("do you want continue the tracking")
                while True:
                    tr=input("if yes enter 'y' or no enter 'n':")
                    if tr=="y" or tr=="Y":
                        return("continue")
                        break
                    elif tr=="n" or tr=="N":
                        print("------------------------------ Thank You --------------------------------")
                        break    
                    else:
                        print("invalid choice")
                
            else:
                print("invalid choice")
            break
    def coimbatore():
        print("select your area \n\t1.rs puram=11 \n\t2.race course==12 \n\t3.gandipuram==13")
        while True:
            A1=int(input("enter the codes as per the area you required:"))
            print("      bus no      starting point            ending point")
            if A1==11:
                print("        111A         RS puram              race course")
                print("        10C          RS puram              gandipuram")
                break
            elif A1==12:
                print("        111A        race course            RS puram")
                print("        10A         race course            gandipuram")
                break
            elif A1==13:
                print("        10C         gandipuram             RS puram")
                print("        10A         gandipuram             race course")
                break
            else:
                print("invalid code")
        print("do you want to continue same city coimbatore")
        while True:
            a=input("if yes enter 'y' or no enter 'n':")
            if a=="y" or a=="Y":
                coimbatore()
                break
            elif a=="n" or a=="N":
                print("do you want to continue the tracking")
                while True:
                    tr=input("if yes enter 'y' or no enter 'n':")
                    if tr=="y" or tr=="Y":
                        return("continue")
                    elif tr=="n" or tr=="N":
                        print("------------------------------ Thank You --------------------------------")
                        break
                    else:
                        print("invalid choice")
               
            else:
                print("invalid choice")
            break         
    def madurai():
        print("select your area \n\t1.mattuthavani==11 \n\t2.kk nagar==12 \n\t3.race course==13")
        while True:
            A1=int(input("enter the codes as per the area you required:"))
            print("      bus no      starting point            ending point")
            if A1==11:
                print("        12A          mattuthavani           kk nagar")
                print("        39A          mattuthavani           race course")
                break
            elif A1==12:
                print("        12A            kk nagar             mattuthavani")
                print("        40C            kk nagar             race course")
                break
            elif A1==13:
                print("        39A          race course            mattuthavani")
                print("        40C          race course            kk nagar")
                break
            else:
                print("invalid code")
        print("do you want to continue same city madurai")
        while True:
            a=input("if yes enter 'y' or no enter 'n':")
            if a=="y" or a=="Y":
                madurai()
                break
            elif a=="n" or a=="N":
                print("do you want continue the tracking")
                while True:
                    tr=input("if yes enter 'y' or no enter 'n':")
                    if tr=="y" or tr=="Y":
                        return("continue")
                    elif tr=="n" or tr=="N":
                        print("------------------------------ Thank You --------------------------------")
                        break   
                    else:
                        print("invalid choice")
               
            else:
                print("invalid choice")
            break

    def area():
        print("welcome to bus tracking programm \nand the cities are :\n\t1.chennai==1\n\t2.coimbatore==2\n\t3.madurai==3")
        while True:
            code=int(input("enter the code according to city you want:"))
            if code==1:
                a=chennai()
                if a=="continue":
                    area()
                    break
                elif a==None:
                    print("***************************** Thank You ******************************")
                    break
                else:
                    print("invalid choice")
            elif code==2:
                a=coimbatore()
                if a=="continue":
                    area()
                    break
                elif a==None:
                    print("***************************** Thank You ******************************")
                    break
                else:
                    print("invalid choice")
            elif code==3:
                a=madurai()
                if a=="continue":
                    area()
                    break
                elif a==None:
                    print("***************************** Thank You ******************************")
                    break
                else:
                    print("invalid choice")
            else:
                ("invalid choice")
    area()
elif pla=="city" or pla=="CITY":
    print("please enter the starting and ending point of the city")
    def chennai1():
        print("ending point cities are:\n\t1.coimbatore=12\n\t2.madurai=13")
        while True:
            y1=int(input("enter the ending city(according to code):"))
            if y1==12:
                print("starting from :chennai and ending at :coimbatore")
                print("      bus no      starting point     starting area       ending point    ending area        timing        bus type")
                print("        1            chennai           koyambedu          coimbatore     gandipuram         6:00am        sitting ")
                print("        2            chennai           koyambedu          coimbatore     gandipuram         8:00am        sleeping")
                print("        3            chennai           kelambakam         coimbatore     singanallur        10:00am       sitting ")
                print("        4            chennai           anna nagar         coimbatore     rs puram           12:00pm       sleeping")
                break
            elif y1==13:
                print("starting from :chennai and ending at :madurai")
                print("      bus no      starting point     starting area       ending point    ending area        timing        bus type")
                print("        1            chennai           koyembedu           madurai       mattuthavani       6:00am        sitting ")
                print("        2            chennai           koyembedu           madurai       mattuthavani       8:00am        sleeping")
                print("        3            chennai           kelambakam          madurai      periyar nilayam     12:00pm       sleeping")
                break
            else:
                print("inavalid choice")
        print("do you want continue same city")
        d=input("if yes type 'y' and if no type 'n':")
        while True:
            if d=="y" or d=="Y":
                chennai1()
            elif d=="n" or d=="N":
                print("do you want continue tracking program or not")
                while True:
                    t=input("if yes type 'y' and if no type 'n':")
                    if t=="y" or t=="Y":
                        return("continue")
                        break
                    elif t=="n" or t=="N":
                        print("=========================== Thank You ============================")
                        break
                    else:
                        print("invalid choice")
            else:
                print("invalid choice")
            break    
    def coimbatore1():
        print("ending point cities are:\n\t1.chennai=11\n\t2.madurai=13")
        while True:
            y=int(input("enter the ending city(according to code):"))
            if y==11:
                print("starting from :coimbatore and ending at:chennai")
                print("      bus no      starting point        starting area       ending point    ending area        timing        bus type")
                print("        1            coimbatore          gandipuram          chennai         koyambedu         6:00am        sitting ")
                print("        2            coimbatore          gandipuram          chennai         koyambedu         8:00am        sleeping")
                break
            elif y==13:
                print("starting from :coimbatore and ending at:madurai")
                print("      bus no      starting point        starting area       ending point     ending area        timing        bus type")
                print("        1           coimbatore           singanallur          madurai        arapalayam         7:00am        sitting")
                print("        2           coimbatore           singanallur          madurai       periyar nilayam     10:00am       sitting")
                break
            else:
                print("invalid choice")
        print("do you want continue same city")
        d=input("if yes type 'y' and if no type 'n':")
        while True:
            if d=="y" or d=="Y":
                coimbatore1()
            elif d=="n" or d=="N":
                print("do you want continue tracking program or not")
                while True:
                    t=input("if yes type 'y' and if no type 'n':")
                    if t=="y" or t=="Y":
                        return("continue")
                        break
                    elif t=="n" or t=="N":
                        print("=========================== Thank You ============================")
                        break
                    else:
                        print("invalid choice")
            else:
                print("invalid choice")
            break       
                
    def madurai1():
        print("ending point cities are:\n\t1.chennai=11\n\t2.coimbatore=12")
        while True:
            y=int(input("enter the ending city(according to code):"))
            if y==11:
                print("starting from :madurai and ending at:chennai")
                print("      bus no      starting point        starting area       ending point    ending area        timing        bus type")
                print("        1           madurai             mattuthavani         chennai         koyambedu         8:00am        sleeping")
                print("        2           madurai             periyar nilayam      chennai         koyambedu         12:00pm       sleeping")
                break
            elif y==12:
                print("starting from :madurai and ending at:coimbatore")
                print("      bus no      starting point        starting area       ending point    ending area        timing        bus type")
                print("        1            madurai            mattuthavani         coimbatore     singanallur        8:00am        sitiing")
                print("        2            madurai            periyar nilayam      coimbatore     singanallur        9:00am        sitting")
                print("        3            madurai            mattuthavani         coimbatore     singanallur        12:00am       sitting")
                break
            else:
                print("invalid choice")
        print("do you want continue same city")
        d=input("if yes type 'y' and if no type 'n':")
        while True:
            if d=="y" or d=="Y":
                madurai1()
            elif d=="n" or d=="N":
                print("do you want continue tracking program or not")
                while True:
                    t=input("if yes type 'y' and if no type 'n':")
                    if t=="y" or t=="Y":
                        return("continue")
                        break
                    elif t=="n" or t=="N":
                        print("=========================== Thank You ============================")
                        break
                    else:
                        print("invalid choice")
            else:
                print("invalid choice")
            break        
    def city():
        print("cities are:\n\t1.chennai=11\n\t2.coimbatore=12\n\t3.madurai=13")
        x=int(input("enter the starting city(according to code):"))
        while True:
            if x==11:
                f=chennai1()
                if f=="continue":
                    city()
                    break
                elif f==None:
                    print("++++++++++++++++++++++++++++ Thank You ++++++++++++++++++++++++++++++")
                    break
                else:
                     print("invalid choice")
            elif x==12:
                f=coimbatore1()
                if f=="continue":
                    city()
                    break
                elif f==None:
                    print("++++++++++++++++++++++++++++ Thank You ++++++++++++++++++++++++++++++")
                    break
                else:
                    print("invalid choice")
            elif x==13:
                f=madurai1()
                if f=="continue":
                    city()
                    break
                elif f==None:
                    print("++++++++++++++++++++++++++++ Thank You ++++++++++++++++++++++++++++++")
                    break
                else:
                    print("invalid choice")
            else:
                print("invalid choice")
    city()            

