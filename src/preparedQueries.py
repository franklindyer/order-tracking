SQL_GET_CLIENT = """
    SELECT name, company, address, email, phone FROM clients WHERE clientID = ?
"""

SQL_GET_PRODUCT = """
    SELECT name, price, notes FROM products WHERE productID = ?
"""

SQL_GET_ORDER = """
    SELECT O.name as name, O.clientID as clientID, O.placed as placed, O.status as status, O.notes as notes, C.name as clientName
    FROM orders O JOIN clients C ON O.clientID = C.clientID
    WHERE O.orderID = ?
"""

SQL_GET_ORDER_ITEMS = """
    SELECT I.productID as productID, I.quantity as quantity, P.name as name, I.quantity*P.price as price
    FROM orderItems I JOIN products P ON I.productID = P.productID
    WHERE I.orderID = ?
"""

SQL_SEARCH_ORDERS = """
    SELECT O.orderID as orderID, O.name as name, O.clientID as clientID, O.placed as placed, O.status as status, C.name as clientName,
           (SELECT sum(P.price * I.quantity) FROM products P JOIN orderItems I ON I.productID = P.productID WHERE I.orderID = O.orderID) as price
    FROM orders O JOIN clients C ON O.clientID = C.clientID
    WHERE TRUE
    ORDER BY placed
    DESC LIMIT 10
"""
