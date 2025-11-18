from supplychain.customer.models import IndividualCustomer


def add_individual_customer(customer_id, name, email, date_of_birth,gender):
    individual=IndividualCustomer(customer_id, name, email, date_of_birth,gender)
    return individual