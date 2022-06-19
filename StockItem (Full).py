
# Individual Coursework: Full Program
# Program Purpose: Operate a stock system for car accessories

# Author: Amin Alhawary
# Start Date: 11.12.21
# Last Updated: 15.1.22

# \\\\\\\\\ STOCKITEM CLASS /////////////


class StockItem:

    stockCategory = "Car Accessories" # Default stock category for all stock items.
    VAT_RATE = 17.5 # Constant to store VAT Rate, which makes it easier for developer to test out different rates.
    typeID = 1 # A number which differenciates between NavSys, StockItem and other child classes

    def __init__(self,code,quantity,price):
        # Item code, quantity and price to be entered when initiaising a stock item.
        self.__code = str(code) # Is a code used to identfy the item.
        self.__quantity = int(quantity) # The quantity in stock of said item.
        self.__price = float(price) # Price of said item.

    def __init__(self,code,quantity,price,name="",desc=""): # Overloading to allow for flexibility
        # Item code, quantity and price to be entered when initiaising a stock item.
        self.__code = str(code) # Is a code used to identfy the item.
        self.__quantity = int(quantity) # The quantity in stock of said item.
        self.__price = float(price) # Price of said item.

        # Added name and description with default values

        self.setName(name) 
        self.setDesc(desc)


    def __str__(self):
        # Returns code, item name, item description, quantity, price and price after VAT in one string.
        return str(("""
____________________________________________
Item: {}
Code: {}
        
Description: {}
Quantity: {}
Price: {:.2f}
Price (after VAT): {:.2f}

""".format(self.getName(), self.__code, self.getDesc(), self.__quantity, self.__price, self.getVAT())))

    def sellStock(self,number:int): # Used to sell wuantity by specified amount.
        if number <= self.__quantity: # Checks if there is enough in stock before changing the quantity.
            self.__quantity = self.__quantity - number # If so, the quantity is reduced by the amount sold.
            print("{} {}(s) sold. Quantity is now {}.".format(number, self.__itemName, self.__quantity)) # Output confirming the new quanitity.
        else: print("Error: {} quantity is too low.".format(self.__itemName)) # Otherwise, an error message is output.

    def increaseStock(self,number):
            if self.__quantity<100: # Checks that quantity is below 100
                self.__quantity = self.__quantity + number # Adding more units
                print("{} {}(s) added to stock. Quantity is now {}.".format(number, self.__itemName, self.__quantity)) # Output confirming the new quanitity.
            else: print("Error: {} quantity is too high.".format(self.__itemName)) # Otherwise, an error message is output.
    # Setters and getters for each variable (code, quantity, itemName, price and desc)
    # Code (code)

    def setCode(self,code):
        self.__code = code

    def getCode(self):
        return self.__code 

    # Quantity (quantity)
    def setQuantity(self,quantity):
       self.__quantity = quantity

    def getQuantity(self):
        return self.__quantity 

    # Item Name (itemName)
    def setName(self,name):
        if name == "":
            self.__itemName = "Unknown Stock Name"
        else: 
            self.__itemName = name
            

    def getName(self):
        return self.__itemName

    # Price (price)
    def setPrice(self,price):
        self.__price = price

    def getPrice(self):
        return self.__price 

    # Item Description (desc)
    def setDesc(self,desc):
        if desc == "":
            self.__desc= "Unknown Stock Description"
        else: 
            self.__desc = desc

    def getDesc(self):
        return self.__desc

    def getVAT(self):
        # Used to calculate the 
        return float(self.__price + (self.__price / (1 + self.VAT_RATE)))

  


# \\\\\\\\\ NAVSYS CLASS /////////////

class NavSys(StockItem):

    typeID = 2 # A number which differenciates between NavSys, StockItem and other child classes
    

    # Overriding six functions: __innit__, setName, setDesc, getName, getDesc, __str__ . To ensure that the output is appropriate to that of an instance of NavSys
    
    def __init__(self,code,quantity,price,name="",desc="",os=""): # Overloading to allow for flexibility
        super().__init__(code,quantity,price,name,desc)
        self.setOSVersion(os)
    
    def getName(self):
        return self.__itemName

    def setName(self,name):
        if name == "":
            self.__itemName = "Navigation System" 
        else: self.__itemName = name

    def getDesc(self):
        return self.__desc
    
    def setDesc(self,desc):
        if desc == "":
            self.__desc= "GeoVision Sat Nav"
        else: self.__desc = desc

    def __str__(self):
        return super().__str__() + "OS Version: "+self.__versionOS

    def getOSVersion(self):
        return self.__versionOS

    def setOSVersion(self,os):
        if os == "":
            self.__versionOS = "Unknown Operating System"
        else: self.__versionOS = os


# \\\\\\\\\ ADDITIONAL CLASSES /////////////

class StylesDecor(StockItem):
    typeID = 3 # A number which differenciates between NavSys, StockItem and other child classes
    def __init__(self,code,quantity,price,name="",desc="",c = ""): # Overloading to allow for flexibility
        super().__init__(code,quantity,price,name,desc)
        self.setColour(c)

    def __str__(self):
        return super().__str__() + "Colour: "+self.getColour()

    def getColour(self):
        return self.__colour

    def setColour(self,c):
        if c == "":
            self.__colour = "Unknown Colour"
        else: self.__colour = c 

class MaintenParts(StockItem):
    typeID = 4 # A number which differenciates between NavSys, StockItem and other child classes
    def __init__(self,code,quantity,price,name="",desc="",m=""): # Overloading to allow for flexibility
        super().__init__(code,quantity,price,name,desc)
        self.setModel(m)

    def __str__(self):
        return super().__str__() + "Model: "+self.getModel()

    def getModel(self):
        return self.__model

    def setModel(self,m):
        if m == "":
            self.__model = "Unknown Model"
        else: self.__model = m 

class BatElect(StockItem):
    typeID = 5 # A number which differenciates between NavSys, StockItem and other child classes
    def __init__(self,code,quantity,price,name="",desc="",p=""): # Overloading to allow for flexibility
        super().__init__(code,quantity,price,name,desc)
        self.setPower(p)

    def __str__(self):
        return super().__str__() + "Power: "+self.getPower()

    def getPower(self):
        return self.__power

    def setPower(self,p):
        if p == "":
            self.__power = "Unknown Power"
        else: self.__power = p 

class Utilities(StockItem):
    typeID = 6 # A number which differenciates between NavSys, StockItem and other child classes

    def __init__(self,code,quantity,price,name="",desc="",m=""): # Overloading to allow for flexibility
        super().__init__(code,quantity,price,name,desc)
        self.setModel(m)

    def __str__(self):
        return super().__str__() + "Model: "+self.getModel()

    def getModel(self):
        return self.__model

    def setModel(self,m):
        if m == "":
            self.__model = "Unknown Model"
        else: self.__model = m 



# \\\\\\\\\ FUNCTIONS AND PROCEDURES TO USE IN MAIN() /////////////

def loadStock(items:list):
    f = open("stock.txt", "r")

    for x in f:
                word = x.split(", ")
                if word[0] == "1":
                    items.append(StockItem(word[1],word[2],word[3],word[4],word[5]))
                elif word[0] == "2":
                    items.append(NavSys(word[1],word[2],word[3],word[4],word[5],word[6]))
                elif word[0] == "3":
                    items.append(StylesDecor(word[1],word[2],word[3],word[4],word[5],word[6]))
                elif word[0] == "4":
                    items.append(MaintenParts(word[1],word[2],word[3],word[4],word[5],word[6]))
                elif word[0] == "5":
                    items.append(BatElect(word[1],word[2],word[3],word[4],word[5],word[6]))
                elif word[0] == "6":
                    items.append(Utilities(word[1],word[2],word[3],word[4],word[5],word[6]))
    f.close()   
    
def updateStock(items:list):
    f = open("stock.txt", "w")
    f.writelines("")

    for i in items:
        f.writelines(str(("\n{}, {}, {}, {:.2f}, {}, {}").format(i.typeID, i.getCode(), i.getQuantity(), i.getPrice(), leaveBlank(i.getName()), leaveBlank(i.getDesc()))))
        if i.typeID == 2:
            f.writelines(", {}".format(leaveBlank(i.getOSVersion())))
        elif i.typeID == 3:
            f.writelines(", {}".format(leaveBlank(i.getColour())))
        elif i.typeID == 4:
            f.writelines(", {}".format(leaveBlank(i.getModel())))
        elif i.typeID == 5:
            f.writelines(", {}".format(leaveBlank(i.getPower())))
        elif i.typeID == 6:
            f.writelines(", {}".format(leaveBlank(i.getModel())))

    f.close()


def leaveBlank(str):
    if str == "Unknown Stock Item":
        return ""
    elif str == "Unknown Stock Description":
        return ""
    elif str == "Unknown Operating System":
        return ""
    elif str == "Unknown Colour":
        return ""
    elif str == "Unknown Model":
        return ""
    elif str == "Unknown Power":
        return ""        
    else: return str


def titleScreen():
        print("""
////////////////////////////////////////////////////////////////////////////
                
                         CAR ACCESSORIES.
                                    
                            -Press enter-



                                                        BY: AMIN ALHAWARY
////////////////////////////////////////////////////////////////////////////////
        """)

def instructions():
        print("""
_________________________________________________________
        Commands:

            1- ADD (Used to add stock items)
            2- SELL (Used to sell stock items)
            3- VIEW (Used to display existing stock items)
            4- END (Used to exit the program)
___________________________________________________________""")


def menuChoice():
    s = numberException("Please enter a number from the list:\n")
    if s == 1: return 1
    elif s == 2: return 2
    elif s == 3: return 3
    elif s == 4: return 4
    else:
         print("Error: No Option Selected, Please try again.")
         return menuChoice()
    print ("\033c")

def editChoice():
    s = numberException("Please enter a number from the list:\n")
    if s == 1: return 1
    elif s == 2: return 2
    elif s == 3: return 3
    elif s == 4: return 4
    elif s == 5: return 5
    elif s == 6: return 6
    elif s == 7: return 7
    else:
         print("Error: No Option Selected, Please try again.")
         return editChoice()
    print ("\033c")

def foundItem(code:str,items:list()): 
    result = 0
    for x in items:
        if code == x.getCode():
            result = 1

    return result

def locateItem(code:str,items:list()):
    count = -1
    for x in items:
        count = count + 1
        if code == x.getCode():
            return count

def typeIDPrompt():
    print("""
What type of item is this?
1- General
2- Navigation System
3- Decorations and Styles
4- Maintenance and Spare Parts
5- Electric and Batteries
6- Utilities
""")
    s = numberException("Please choose from list\n")
    while s > 6 or s < 1:
        print("Error: Invalid Option\n")
        s = numberException("Please choose from list\n")
    
    return s

def ADD(items:list):

    code = str(inputCode())
    if foundItem(code,items):
        temp = locateItem(code,items)
        print(items[temp])
        num = int(inputNum("How many units would you like to add?\n"))
        items[temp].increaseStock(num)
        updateStock(items)
    else:
        name = str(inputText(1))
        desc = str(inputText(2))
        s = typeIDPrompt()
        price = float(inputPrice())
        num = int(inputNum("How many units would you like to add?\n"))
        if s == 1:
            items.append(StockItem(code,0,price,name,desc))
        elif s == 2:
            items.append(NavSys(code,0,price,name,desc))
        elif s == 3:
            items.append(StylesDecor(code,0,price,name,desc))
        elif s == 4:
            items.append(MaintenParts(code,0,price,name,desc))
        elif s == 5:
            items.append(BatElect(code,0,price,name,desc))
        else:
            items.append(Utilities(code,0,price,name,desc))

        temp = locateItem(code,items)
        items[temp].increaseStock(num)
        updateStock(items)

def SELL(items:list):
    code = str(inputCode())
    if foundItem(code,items):
        temp = locateItem(code,items)
        print(items[temp])
        num = int(inputNum("How many units would you like to sell?\n"))
        items[temp].sellStock(num)
        updateStock(items)
    else:
        print("Error: This item does not exist.")
        s = input()

def VIEW(items:list):
    print ("\033c")
    for x in items:
        print(x)
        
    print("____________________________________________")
    s = input()
    z = numberException("Would you like to edit an item? (1- Yes, 2- No)\n")
    while (z != 2) & (z!= 1):
        print("Error: No Option Selected, Please try again")
        z = numberException("Would you like to edit an item? (1- Yes, 2- No)\n")
    
    if z == 1:

        if password() == 0:
            return 1
        code = str(inputCode())
        if foundItem(code,items):
            temp = locateItem(code,items)
            print(items[temp])
            print("""
_______________________________
What would you like to edit?
1- Rename item
2- Change code
3- Change discription
4- Change price
5- Delete item
6- Advanced
7- BACK
_______________________________
""")    
            choice = editChoice()
            if choice == 7:
                return 1
            elif choice == 1:
                items[temp].setName(str(inputText(1)))
                print("Name changed.")
            elif choice == 2:
                code = inputCode()
                if foundItem(code,items):
                    print("Error: Code already in use.")
                else: 
                    items[temp].setCode(code)
                    print("Code changed.")
            elif choice == 3:
                items[temp].setDesc(str(inputText(2)))
                print("Description.")
            elif choice == 4:
                items[temp].setPrice(inputPrice())
                print("Price changed.")
            elif choice == 5:
                items.pop(temp)
                print("Item has been rmeoved.")
                updateStock(items)
            else:
                if items[temp].typeID == 1:
                    print("Sorry, advanced options aren't available for this item")
                else:
                    advanced(items[temp])

            updateStock(items)
        else: 
            print("Error: This item does not exist.")
            s = input()
        s = input()

def advanced(item:StockItem):
    if item.typeID == 2:
           print("Navigation System")
           print("OS: {}".format(item.getOSVersion()))
           z = numberException("Would you like to change OS Version? (1- Yes, 2- No)\n")
           while (z != 2) & (z!= 1):
                print("Error: No Option Selected, Please try again")
                z = numberException("Would you like to change OS Version?? (1- Yes, 2- No)\n")
           if z == 1:
               item.setOSVersion(inputText(3))
    elif item.typeID == 3:
            print("Decorations and Styles")
            print("Colour: {}".format(item.getColour()))
            z = numberException("Would you like to change colour? (1- Yes, 2- No)\n")
            while (z != 2) & (z!= 1):
                print("Error: No Option Selected, Please try again")
                z = numberException("Would you like to change colour? (1- Yes, 2- No)\n")
            if z == 1:
               item.setColour(inputText(3))
    elif item.typeID == 4:
            print("Maintenance and Spare Parts")
            print("Model: {}".format(item.getModel()))
            z = numberException("Would you like to change model? (1- Yes, 2- No)\n")
            while (z != 2) & (z!= 1):
                print("Error: No Option Selected, Please try again")
                z = numberException("Would you like to change model? (1- Yes, 2- No)\n")
            if z == 1:
               item.setModel(inputText(3))
    elif item.typeID == 5:
            print("Electric and Batteries")
            print("Power: {}".format(item.getPower()))
            z = numberException("Would you like to change power? (1- Yes, 2- No)\n")
            while (z != 2) & (z!= 1):
                print("Error: No Option Selected, Please try again")
                z = numberException("Would you like to change power? (1- Yes, 2- No)\n")
            if z == 1:
               item.setPower(inputText(3))
    elif item.typeID == 6:
            print("Utilities")
            print("Model: {}".format(item.getModel()))
            z = numberException("Would you like to change model? (1- Yes, 2- No)\n")
            while (z != 2) & (z!= 1):
                print("Error: No Option Selected, Please try again")
                z = numberException("Would you like to change model? (1- Yes, 2- No)\n")
            if z == 1:
               item.setModel(inputText(3))


def password():
    print("You need authentication to proceed")
    print("Enter password:")
    ps = input()
    if ps == "password":
        return 1
    else:
        print("Error: Incorrect Password")
        return 0

def inputCode():
    s = notNullSTR("Please enter item code:\n")
    if len(s) > 10:
        print("Error: Invalid Code, Maximum Length = 10.")
        return inputCode()
    elif ("," in s):
        print("Error: Invalid Code, can't contain commas.")
        return inputCode()
    else: return s

def inputText(n:int):
    
    if n == 1:
        s = input("Enter item name: (OPTIONAL)(MAX = 15)(NO COMMAS)\n")
        if ("," in s) | (len(s) > 15):
            print("Error: Invalid Name, Please try again.")
            return inputText(1)
    elif n == 2:
        s = input("Enter descrption: (OPTIONAL)(MAX = 25)(NO COMMAS)\n")
        if ("," in s) | (len(s) > 25):
            print("Error: Invalid Description, Please try again.")
            return inputText(2)
    else:
        s = input("Enter new details: (MAX = 15)(NO COMMAS)\n")
        if ("," in s) | (len(s) > 15):
            print("Error: Invalid, Please try again.")
            return inputText(1)
    return s
    
def inputPrice():
    try:
        s:float = float(input("Please enter item price:\n"))
    except ValueError:
        print("Error: Invalid, Please only enter numbers.")
        return inputPrice()
    if s <= 0:
        print("Error: Price can't be zero or less")
        return inputPrice()
    else: return s

def inputNum(msg):
    s = int(numberException(msg))
    if s <= 0:
        print("Error: Number can't be zero or less")
        return inputNum(msg)
    else: return s

def numberException(msg:str):

    try:
        s:int = int(input(msg))
    except ValueError:
        print("Error: Invalid, Please only enter numbers.")
        return numberException(msg)

    return s

def notNullSTR(msg:str):
    n = input(msg)
    if n == "":
        print("Error: Null Entry, Please try again.")
        return notNullSTR(msg)
    else: return n

def writeItem(item:StockItem):
    f = open("stock.txt", "a")
    s = item.typeID+","+item.getCode()+","
    f.writelines()

# \\\\\\\\\ MAIN() /////////////
class Main():
    items:list = []
    loadStock(items)


    titleScreen()
    x = 1
    while x == 1:
        s = input()
        print ("\033c")
        instructions()
        choice = menuChoice()
        if choice == 4:
            break
        elif choice == 1: ADD(items)
        elif choice == 2: SELL(items)
        else: VIEW(items)
    	


    
