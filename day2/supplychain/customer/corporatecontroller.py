from supplychain.customer.models import CorporateCustomer

def add_corporate_customer(customer_id, name, email, company_type, tax_id):
    corporate=CorporateCustomer(customer_id, name, email, company_type, tax_id)
    return corporate