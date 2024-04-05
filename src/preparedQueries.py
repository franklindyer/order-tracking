SQL_GET_CLIENT = """
    SELECT name, company, address, email, phone FROM clients WHERE clientID = ?
"""

SQL_GET_PRODUCT = """
    SELECT name, price, notes FROM products WHERE productID = ?
"""
