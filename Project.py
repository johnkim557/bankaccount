#create empty array for objects
customers =[]
bankAccounts =[]
employees = []
services = []


class Customer():
    #constructor
    #include paramaters such as first name, last name, address, balance
    #type of account
    #withdraw/deposit method
  
    def __init__(self, first_name, last_name, address,balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.balance = balance
        customers.append(self.__dict__)
        customers.append()
        #setter method
        
        #input property decorators for setter
    def set_name(self):
        x = input('Input your first name: ')
        y = input('Input your last name: ')
        #must be a string or output an error
        self.first_name = x
        self.last_name = y

        #getter method
    def get_name(self):
        return self.first_name+ " "+ self.last_name
    
class BankAccount(Customer):
    
    def __init__(self,balance=0):
        self.balance= balance
        Customer.__init__(self,first_name,last_name,address,balance=0)
        self.first_name = Customer.first_name
        self.last_name = Customer.last_name
        self.address = Customer.address
        bankAccounts.append(self.__dict__)
        
    def deposit(self,input_amount):
        self.balance += input_amount

    def withdraw():
        if self.balance <0:
            print('Funds Unavailable for Withdrawal')
        elif self.balance <= input_amount:
            print('Funds Unavailable for Withdrawal')
        else:
            self.balance = self.balance - input_amount
            print("Your Updated Balance: $",self.balance)
            
class Employees():
     #first name, last name, employee id, department, salary, job status, 
    
    def __init__(self, name, employee_id, department, salary, hire_date):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
        self.hire_date = hire_date
        employees.append(self.__dict__)
        #add settings decorators for data types.
    def give_raise(self, raise_amount):
        self.salary += raise_amount
        print("Updated Employee Salary: ",self.salary)
    
    
class Services():

    def __init__(self, name, address, birth_date, social_security,credit_card=None,loan=None):
        self.name = name
        self.address= address
        self.birth_date = birth_date
        self.social_security = social_security
        self.credit_card = credit_card
        self.loan = loan
        services.append(self.__dict__)
    def view_info(self):
        print("Customer Information:")
        print("")
        print("Name: ")
        print("Address: ")
        print("Birth Date: ")
        print("Social Security: XXX-XXX-{}",self.social_security[:-4])
        print("Loan: ")
        print("Credit Card: ")
    #setter method
    def select_credit_card(self):
        x = input("SELECT CREDIT CARD")

    
    def raise_credit_limit(self, amount):

    
    #loans, credit cards



#convert information into pandas dataframe apply efficient pythonic processes.

#convert dataframe to csv or sql
df_cust = pd.DataFrame(customers)
df_bankAcc = pd.DataFrame(bankAccounts)
df_emp = pd.DataFrame(employees)
df_services = pd.DataFrame(services)


df_cust.to_csv('customers.csv',index = False)
df_bankAcc.to_csv('BankAccounts.csv', index = False)
df_emp.to_csv('employees.csv',index = False)
df_services.to_csv('services.csv',index = False)

