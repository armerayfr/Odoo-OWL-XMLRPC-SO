import xmlrpc.client
import time

class OdooXMLRPCClient:
    def __init__(self, url, db, username, password, retries=10, delay=3):
        self.url = url
        self.db = db
        self.username = username
        self.password = password

        self.common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        # self.uid = self.common.authenticate(db, username, password, {})
        self.models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

        for i in range(retries):
            try:
                self.uid = self.common.authenticate(db, username, password, {})
                if self.uid:
                    break
            except Exception as e:
                print(f"Retrying Odoo connection... ({i+1}/{retries})")
                time.sleep(delay)
        else:
            raise Exception("Could not connect to Odoo after multiple retries")


    def call(self, model, method, args=None, kwargs=None):
        args = args or []
        kwargs = kwargs or {}
        return self.models.execute_kw(
            self.db, self.uid, self.password,
            model, method, args, kwargs
        )
