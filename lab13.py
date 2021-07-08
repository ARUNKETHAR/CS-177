#problem 1: write class person
#Copy your class person from the prelab, and make the required modifications as instructed in the lab
class person:
    def __init__(self, name, phone, salary, nationality, supervisor):
        self.name = name
        self.phone = phone
        self.salary = salary
        self.nationality = nationality
        self.supervisor = supervisor
    def print_business_card(self):
        print("Name: ", self.name)
        print("Phone: ", self.phone)
        print("Salary: ", self.salary)
        print("Supervisor: ", self.supervisor)
    def calculate_tax(grace):
        if(self.nationality == "US"):
            taxPrice = 0.2 
        else:
             taxPrice = 0.35
        cost = ((self.salary * 12) * taxPrice)
        print("Tax: ", cost)

#problem 2: write class employee
#Copy your class employee from the prelab, and make the required modifications as instructed in the lab
class employee(person):
    def __init__(self, name, phone, salary, nationality, supervisor):
        erson.__init__(self, name, phone, salary, nationality, supervisor)
    def print_business_card(self):
        print("Name: ", self.name)
        print("Phone: ", self.phone)
        print("Title: Employee")
        print("Supervisor: ", self.supervisor)
        


#problem 3: write class manager
##Copy your class manager from the prelab, and make the required modifications as instructed in the lab
class manager(person):
    def __init__(self, name, phone):
        person.__init__(self, name, phone)
    def print_business_card(self, name, phone):
        person.print_business_card(self, name, phone)
        print("Title: Manager")
    def calculate_tax(grace):
        tax = self.salary
        print(tax)
    


def main():
    p1 = person('Peter Parker','4445556666', 1500, 'US')
    e1 = employee('Clark Kent','5556667777', 2000, 'US')
    e2 = employee('Benedict Bumberbatch','8889990000', 2550, 'UK')
    m1 = manager('Bruce Wayne','9998887777', 10000, 'US')
    m2 = manager('Tony Stark','1112223333', 5000, 'US')
        
    e1.set_supervisor(m1)
    e2.set_supervisor(m2)
    
    myList = [p1,e1,e2,m1,m2]
    for i in myList:
        i.print_business_card()
        print('Tax: ',i.calculate_tax(300),'\n')
        
 
main()
