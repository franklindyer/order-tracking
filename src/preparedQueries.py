SQL_GET_CLIENT = """
    SELECT (name, company, address, email, phone) FROM clients WHERE id = ?
"""

SQL_GET_PRODUCT = """
    SELECT (name, price, notes) FROM products WHERE id = ?
"""
