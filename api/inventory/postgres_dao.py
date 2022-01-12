from api.inventory.models import Item
from api import db



class postres_dao:

    def create_product(self, product_code, name, price, weight):
        db.session.add(Item(
            product_code=product_code,
            name=name,
            price=price,
            weight=weight))
        self.commit()
    
    
    def get_product(self, product_code):
        Item.query(product_code=product_code)
        self.commit()
        
    def update_product():
        pass

    def delete_product():
        pass

    def commit(self):
        db.session.commit()