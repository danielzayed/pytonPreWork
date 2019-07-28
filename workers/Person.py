
import re

class InValidVariable(Exception) :
    def __init__  (self,data) :
        self.data=data

class Person :
    id=-1 ;
    @staticmethod
    def checkemail(email):
        return  re.match("^[\w+]@[\w+\.]+hwltd.com$", email)


    def __init__(self, first_name, last_name,YearOfBirth,email,phone,address):
       self.email=email
       self.Address=address
       self.first=first_name
       self.last=last_name
       self.Year=YearOfBirth
       self.phone=phone
       self.address=address
       self.id=Person.id
       self.phones=[]


    @classmethod
    def  New_Person(cls,first_name,last_name,YearOfBirth,email,phone,address) :
            cls.id=Person.id+1
            try:
                if  not Person.checkemail(email):
                    raise InValidVariable("Email Entered is Invalid!!!")
            except InValidVariable as e:
                print("Received error: ", e.data)
            return cls(first_name,last_name,YearOfBirth,email,phone,address)


    def add_phone(self,new_phone):
        self.phones.append(new_phone)
    def remove_phone(self,del_phone):
        self.phones.remove(del_phone)

class Phone :
    @staticmethod
    def checkphone(phone):
        x = re.match("^[0-9]| \+ ([0-9]|-)*$ ",phone )
        if x:
            return True
        return False

    def __init__(self,phone):
        try:
          if not  Phone.checkphone(phone):
              raise InValidVariable("Phone Entered is Invalid!!!")

        except InValidVariable as e :
            print("Received Erorr: ",e.data)

        self.phone=phone





class Address:

    def __init__ (self,Country="Israel",City="Jersaluem" ):
        self.Country=Country
        self.City=City

    def _ret_otherDetails(self):
        raise NotImplementedError("Abstract class : this Method is not implemented")

    def ret_address(self):
        return '{} {} {}'.format(self.Country,self.City,self._ret_otherDetails())



class StreetAddress(Address) :
    def __init__(self,Country,City,Street,Number):
        super().__init__(Country,City)
        self.street=Street
        self.number=Number

    def _ret_otherDetails(self):
        return '{} {}'.format(self.street,self.number)




class PobAddress(Address):

   def __init__(self, Country,City,PostOfficeNumber):
       super().__init__(Country,City)
       self.number=PostOfficeNumber
   def _ret_otherDetails(self):
        return self.number




