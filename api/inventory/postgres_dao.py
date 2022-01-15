from api.inventory.models import Base, Item
from api import db
from dataclasses import asdict

class postgres_dao:
    def __init__(self):
        pass

    def get_product_field_names(self):
        return Item.__table__.columns.keys()

    def create_product(self, name, price, weight, description=None):
        product = Item(
                    name=name,
                    price=price,
                    weight=weight,
                    description=description)
        db.session.add(product)
        self.commit()
        return asdict(product)
    
    
    def get_product(self, id):
        product = Item.query(id=id).one()
        return asdict(product)
        
    def update_product(self, id, fields):
        product = Item.query.filter_by(id=id).one()
        product_dict = asdict(product)
        for field in fields:
            if field in product_dict:
                product.__setattr__(field, fields[field])
        self.commit()
        return asdict(product)

    def delete_product(self,id):
        Item.query.filter_by(id=id).one().delete()
        self.commit()

    def get_all_product(self):
        return Item.query.all()

    def commit(self):
        db.session.commit()