from exceptions import EmailException
from supplychain.customer.models import IndividualCustomer


def add_individual_customer(customer_id, name, email, date_of_birth,gender):
    try:
        individual=IndividualCustomer(customer_id, name, email, date_of_birth,gender)
    except EmailException as e:
        print(f"Error adding individual customer: {e}")
        return None
    return individual