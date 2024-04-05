import os, sqlite3
from multiprocessing.pool import ThreadPool

from preparedQueries import *

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class DatabaseManager:
    def __init__(self, dbname):
        self.dbname = dbname
        self.readPool = ThreadPool(processes=10)
        self.writePool = ThreadPool(processes=1)
        self.connect()

    def connect(self):
        self.conn = sqlite3.connect(self.dbname, check_same_thread=False)
        self.conn.row_factory = dict_factory

    def commit(self):
        self.conn.commit()

    def cur(self):
        cur = self.conn.cursor()
        cur.row_factory = dict_factory
        return cur

    def poolQuery(self, query, args=()):
        cur = self.cur().execute(query, args)
        res = [x for x in cur.fetchall()]
        cur.close()
        return (res if len(res) > 0 else None)

    def poolExecute(self, query, args=()):
        cur = self.cur().execute(query, args)
        cur.close()
        self.commit()

    def query(self, query, args=()):
        return self.readPool.apply(self.poolQuery, (query, args,))

    def execute(self, query, args=()):
        return self.writePool.apply(self.poolExecute, (query, args,))



    def getClient(self, clientID):
        return self.query(SQL_GET_CLIENT, (clientID,))[0]

    def getProduct(self, productID):
        return self.query(SQL_GET_PRODUCT, (productID,))[0]

    def getOrder(self, orderID):
        order = self.query(SQL_GET_ORDER, (orderID,))[0]
        order["items"] = self.query(SQL_GET_ORDER_ITEMS, (orderID,))
        return order
