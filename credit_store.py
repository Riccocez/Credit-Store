 

def credit():

    #Restrictions of data

    N_limits = (3,100)
    C_limits = (5,1000)
    P_limits = (1,1000)
    I_limits = (3,100,2000)
    L = []

    # Configuration of Cases

    print ("Credit Store Code")
    
    dataset_size = str(raw_input("Size of data set? ((s)mall/ (l)arge) "))
    

    if dataset_size.lower() == "s":
        upper_ilimit = I_limits[1]
    elif dataset_size.lower() == "l":
        upper_ilimit = I_limits[2]
    else:
        print "Dataset configuration Not Found"
        return


    N = int(raw_input("Number of cases?"))

    

    if N >= N_limits[0] and N<= N_limits[1]:

        I = int(raw_input("Number of items in store?"))
        C_N = int(raw_input("Credit Amount?"))

        if I >= I_limits[0] and I <= upper_ilimit:

            
        
            for item in range(0,I):
                
                checker = 0                 
                while checker != 1:
                    
                    item_price = int (raw_input("price of item " + str(item+1) + " :"))

                    if item_price >= P_limits[0] and item_price <= P_limits[1]:
                        checker = 1

                        L.append(item_price)
                        
                    else:
                        print "Unvalid price"
                        print "Include a price between", P_limits[0],"and",P_limits[1]


    l_size= len(L)
    index = 0

    print "size of list :",l_size

    for item_1 in range(index,l_size):
        #index +=1
        print "item 1 value :",item_1
        for item_2 in range(index+1 ,l_size):
        #aux_index += 1
            print "item 2 value :",item_2
            if L[item_1] + L[item_2] == C_N:
                print "Position of items for case",N, " :", item_1, item_2
                return
            

    return


