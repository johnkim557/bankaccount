# Bank Account Class Project


## Introduction

The python file included within the github repository holds multiple Bank Account classes that
allow the creation of instances. Four different classes have been produced showcasing inheritance amongs some
but not all classes to eliminate algorithmic redundancy. The customer class allows the user to input initial arguements or attributes which will be appended into an empty 'customers' array which will be used to be converted a pandas dataframe and then a csv file afterwards. The same procedure will be used for the remaining classes to output a csv file that will retain information of the instances created by the user. 


### Customer
To create an instance of the customer class, the user must first input the required arguements to access the
class' methods. The first name, last name, and address need to be stored an as initial arguements. Afterwards,
apply the instance.methods approach to set a new name or get the existing name of the instance.


### Bank Account
The bank account class provides unique methods that allow the user to deposit or withdraw a two decimal float number
amount. A constuctor is not needed due to inheriting the customer class' properties. As a result, the user must
input the same initial arguements as those inputted when creasting a customer instance. To access the methods within the bank account class, apply the instance.method approach to increase or decrease the instance's balance.


### Services

The services class allows the user to choose the available credit card options from Sapphire to Black. Each option witholds
a different amounts of a usable credit. The credit card user can use the card for further purchases or credit balance payments through
the available methods. An increase in credit can also be made after the customer has proved a solid credit history with an acceptable
credit score.

## Data ETL and Storage
The indiviudal instances will be stored within an empty list that will be converted into a pandas dataframe and then into a csv file afterwards.
A data warehouse of all changes will be stored within the same csv file.

### Possible Improvements
Change the output to an SQL database. 
