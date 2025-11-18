from enum import Enum
from abc import ABC, abstractmethod

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

class CompanyType(Enum):
    LLC = "LLC"
    CORPORATION = "Corporation"
    PARTNERSHIP = "Partnership"
    SOLE_PROPRIETORSHIP = "Sole Proprietorship"

#abstract class
class Customer(ABC):
    #static variable
    payment_terms = "Net 30 Days"
    def __init__(self, customer_id, name, email):
        self._customer_id = customer_id
        self._name = name
        self._email = email
    @abstractmethod
    def calculate_discount(self):
        pass    


#inheritance
class IndividualCustomer(Customer):
    def __init__(self, customer_id, name, email, date_of_birth,gender):
        super().__init__(customer_id, name, email)
        self.__date_of_birth = date_of_birth
        self.__gender = gender
    def calculate_discount(self):
        return 0.05  # 5% discount for individual customers

class CorporateCustomer(Customer):
    def __init__(self, customer_id, name, email, company_type, tax_id):
        super().__init__(customer_id, name, email)
        self.__company_type = company_type
        self.__tax_id = tax_id
    def calculate_discount(self):
        return 0.10  # 10% discount for corporate customers