from Cases import Case



print "Credit Store Challenge"


#cases = Case()
L_cases = {}


#Setting configuration of credit store
size = Case.validation("Size of data set? ((s)mall / (l)arge) ", "string", "D")

print "size :",size

N = Case.validation("Number of cases? ", "integer","N")
print "cases :", N

#Defining case_object settings
for n_case in range(0,N):

    object_case = Case()
    C = object_case.validation("Credit Amount for case "+ str(n_case+1)+" ?","integer","C")
    object_case.C = C
    print "credit amount :",C

    object_case.set_dataset(size)
    
    I= object_case.validation("Number of items in store for case "+ str(n_case+1)+" ?","integer","I")
    print "item numbers :", I
    
    object_case.items_list = object_case.price_items("Price of item ","integer",I)

    items = object_case.find_items()

    print "Position of items for case ", n_case, " :", items[0]," , ", items[1]

    #L cases[str(n_case)]= items

print L_cases    








