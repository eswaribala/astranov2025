from supplychain.customer.models import CorporateCustomer
from exceptions import EmailException

def add_corporate_customer(customer_id, name, email, company_type, tax_id):
    try:
        corporate=CorporateCustomer(customer_id, name, email, company_type, tax_id)
    except EmailException as e:
        print(f"Error adding corporate customer: {e}")
        return None 
    return corporate