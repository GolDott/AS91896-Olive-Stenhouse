detail_file = "details.txt"

class hire_details:
    def __init__(self, name, receipt, item, quantity): #this is here to define what is required in the class
        self.name = name
        self.receipt = receipt
        self.item = item
        self.quantity = quantity

    def readable_details(self): #these details are easy to read for someone viewing the system and can be printed on command
        print(f"Name: {self.name}") #each line is a detail of the requested hire details
        print(f"Receipt: {self.receipt}")
        print(f"Item: {self.item}")
        print(f"Quantity: {self.quantity}")

    def logged_details(self): #this allows the system to put someones hire details into the text file so that it will not be lost
        return f"{self.name} {self.receipt} {self.item} {self.quantity}"

def new_hire(): #When someone hires something new this code will run and ensure that the correct details are put in
    name = ""
    receipt = 0
    item = ""
    quantity = 0
    while name == "":
        new_input = input("Name: ")
        if not new_input.strip():
            print("Name cannot be empty")
        else:
            name = new_input
            while receipt == 0:
                new_input = input("Receipt: ")
                if new_input.strip() == "" or (new_input.isdigit() == False):
                    print("Receipt cannot be empty and must be a number")
                else:
                    receipt = new_input
                    while item == "":
                        new_input = input("Item: ")
                        if new_input.strip() == "":
                            print("Item cannot be empty")
                        else:
                            item = new_input
                            while quantity == 0:
                                new_input = input("Quantity: ")
                                if new_input.strip() == "" or (new_input.isdigit() == False) or int(new_input) < 1 or int(new_input) > 500:
                                    print("Quantity cannot be empty, must be a number, and must be between 1 and 500")
                                else:
                                    quantity = int(new_input)

    print(f"Name: {name}, Receipt: {receipt}, Item: {item}, Quantity: {quantity}")

new_hire()

#print(noah.readable_details())

#file_append.write(noah.logged_details())
