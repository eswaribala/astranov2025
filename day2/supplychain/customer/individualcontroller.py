from exceptions import EmailException
from supplychain.customer.models import IndividualCustomer
from exceptions.validate import validate_email

def add_individual_customer(customer_id, name, email, date_of_birth,gender):
    try:
        if( not validate_email(email)):
            raise EmailException("Invalid email format")
        individual=IndividualCustomer(customer_id, name, email, date_of_birth,gender)
    except EmailException as e:
        print(f"Error adding individual customer: {e}")
        return None
    return individual