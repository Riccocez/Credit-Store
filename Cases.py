
class Case():

    def __init__(self, N_limits = (3,100), C_limits = (5,1000), P_limits = (1,1000), I_limits = (3,100,2000)):
       

        self.N_limits = N_limits         #Number of cases
        self.C_limits = C_limits         #Credit Amount 
        self.P_limits = P_limits         #Price of item
        self.I_limits = I_limits         #Items

        self.dataset_size = 0
        self.items_list = []
        self.C = 0

        

    def validation(self,string,type_input, feature):

        valid = "wrong"

            
        while (valid != "ok"):

            variable = raw_input(string)
            

            if type_input == 'string':

                variable = str(variable)

                valid = self.set_dataset(variable)

                    
            elif type_input == 'integer':


                variable = int(variable)
                valid = self.set_value(variable, feature)
                

            if valid == "wrong":
                
                self.validation_wrong(feature)           

        return variable

    def validation_wrong(self,feature):

        print "Invalid input"
        print "feature", feature

        if feature == "D":
            
            print "Choose (s)mall or (l)arge "
            
        else:

            (lower_limit, upper_limit) = self.value_type_limits(feature)
        
            print "Include an input between ", str(lower_limit), " and ", str(upper_limit)

        return

    def set_dataset(self, size):

        if size.lower() == "s":
            
            self.dataset_size = self.I_limits[1]
            valid = "ok"
            
        elif size.lower() == "l":
            
            self.dataset_size = self.I_limits[2]
            valid = "ok"
            
        else:
            
            print "Dataset configuration Not Found, choose 's' or 'l' "
            valid = "wrong"

            
        return valid

    def value_type_limits(self,value_type):

        lower_limit = 0
        upper_limit = 0

        if value_type == "N":

            lower_limit = self.N_limits[0]
            upper_limit = self.N_limits[1]
            
        elif value_type == "I":

            lower_limit = self.I_limits[0]
            upper_limit = self.dataset_size
            
        elif value_type == "C":
  
            lower_limit = self.C_limits[0]
            upper_limit = self.C_limits[1]
            
        elif value_type == "P":

            lower_limit = self.P_limits[0]
            upper_limit = self.P_limits[1]

        return lower_limit,upper_limit

        
    def set_value(self,value, feature):

        value_limits = self.value_type_limits(feature)

        if value >= value_limits[0] and value <= value_limits[1]:

            valid = "ok"
        else:

            valid = "wrong"

        return valid

    def price_items(self,string,type_value,value):
         

        for price_i in range(0,value):
            
            item_price = self.validation(string + str(price_i+1) + "?","integer","P")
            self.items_list.append(item_price)
        return
            
    def find_items(self)

        l_size = len(self.items_list)
        index = 0

        for item_1 in range(index,l_size):

            for item_2 in range(index+1, l_size):

                if self.items[item_1] + self.items[item_2] = self.C:

                    return (item_1,item_2)
        return


    #Class


    #limits

    #acquire info


    #validate info

    #case checkout

    

