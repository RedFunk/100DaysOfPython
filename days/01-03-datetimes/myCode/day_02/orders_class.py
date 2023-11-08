from datetime import datetime
import pickle
import os

filename = "order_data.pkl"

from enum import auto
class Orderstate():
    ORDERD = auto()
    CONFIRMED = auto()
    RECIVEDSUBORDER = auto()
    RECIVEDSUBBILL = auto()
    RECIVEDFULLORDER = auto()
    RECIVEDFULLBILL = auto()
    COMPLETE = auto()
    ARCHIVED = auto()

class Order:
    
    deliverys = 1
    confirm_datetime = 0
    recived_datetime = 0
    recivedBill_datetime = 0
    completet_datetime = 0
    archived_datetime = 0
    
    def __init__(self, name, amount=0, description=""):
        self.name = name
        self.amount = amount
        self.description = description
        self.buy_datetime = datetime.today()
        self.state = Orderstate.ORDERD
        
    def confirmed(self):
        self.confirm_datetime = datetime.today()
        self.state = Orderstate.CONFIRMED
    
    def recived(self):
        self.recived_datetime = datetime.today()
        self.state = Orderstate.RECIVEDFULLORDER
        
    def recivedBill(self):
        self.recivedBill_datetime = datetime.today()
        self.state = Orderstate.RECIVEDFULLBILL
        
    def completet(self):
        self.completet_datetime = datetime.today()
        self.state = Orderstate.COMPLETE
        
    def archived(self):
        self.archived_datetime = datetime.today()
        self.state = Orderstate.ARCHIVED
        
    def print(self):
        print("-" * 20)
        print(f"Order: {self.name}")
        self.pit("Orderd at: ", self.buy_datetime)
        self.pit("Confirmed at: ", self.confirm_datetime)
        self.pit("Recived Order at: ", self.recived_datetime)
        self.pit("Recived Bill at: ", self.recivedBill_datetime)
        self.pit("Completed at: ", self.completet_datetime)
        self.pit("Archived at: ", self.archived_datetime)
        print("-" * 20)
    
    def pit(self, text, date):
        print(text, end="")
        if(date == 0):
            print("No Information.")
        else:
            print(date.strftime("%d-%b-%Y | %H:%M:%S"))

def dataExists():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Change the current working directory to the script's location
    os.chdir(script_dir)

    # Get the current working directory (the script's folder)
    current_directory = os.getcwd()

    # Define the file path to check
    file_path = os.path.join(current_directory, filename)

    # Check if the file exists
    if os.path.exists(file_path):
        print(f"{filename} exists in the script's folder.")
        return True
    else:
        print(f"{filename} does not exist in the script's folder.")
        return False

if __name__ == "__main__":
    if(not dataExists()):
        o1 = Order("EM 966355",154.60,"Material Absackanlage")
        o2 = Order("Kablan 96432422",832.00,"Material IQS: 2225343")
    else:
        with open(filename, 'rb') as inp:
            o1 = pickle.load(inp)
            o2 = pickle.load(inp)

    o1.print()
    o2.print()
    
    with open(filename, 'wb') as outp:
        pickle.dump(o1, outp, pickle.HIGHEST_PROTOCOL)
        pickle.dump(o2, outp, pickle.HIGHEST_PROTOCOL)
        