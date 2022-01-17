from os import name

from flask.helpers import flash
from api import db
from dataclasses import dataclass

class Base(db.Model):
    __abstract__  = True
    
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())
    id = db.Column(db.Integer(), primary_key=True)

@dataclass
class Item(Base):
    id: int
    name:  str
    price:  float
    weight:  float
    quantity: int
    description: str
    
    __tablename__ = "Items"
    __table_args__ = {'extend_existing': True} 
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    weight = db.Column(db.Numeric, nullable=False)
    quantity = db.Column(db.BigInteger, nullable=False, default=0)
    description = db.Column(db.Text, nullable=True)
    # db.UniqueConstraint(product_code)
    # brand_id
    # supplier_id
    # description
    # is_active
    # deleted

    
class Shipment(Base):
    __tablename__ = "Shipments"
    __table_args__ = {'extend_existing': True} 
    # shipment_id
    # shipped
    pass

class Shipment_Items(Base):
    __tablename__ = "ShipmentItems"
    __table_args__ = {'extend_existing': True} 
    pass

class Supplier(Base):
    __tablename__ = "Suppliers"
    __table_args__ = {'extend_existing': True} 
    # code
    # name
    # type
    pass

class Price_Record(Base):
    __tablename__ = "PriceRecords"
    __table_args__ = {'extend_existing': True} 
    pass

class Item_Attribute(Base):
    __tablename__ = "ItemAttributes"
    __table_args__ = {'extend_existing': True} 
    pass


class Item_Attribute_Type(Base):
    __tablename__ = "ItemAttributeTypes"
    __table_args__ = {'extend_existing': True} 
    # attribute_name
    pass

class Warehouse(Base):
    __tablename__ = "Warehouses"
    __table_args__ = {'extend_existing': True} 
    # warehouse_code
    # warehouse_name
    pass
class Category(Base):
    __tablename__ = "Categories"
    __table_args__ = {'extend_existing': True} 
    pass
class Brand(Base):
    __tablename__ = "Brands"
    __table_args__ = {'extend_existing': True} 
    # manufacturer_id
    # brand_code
    # brand_name
    pass

class Manufacturer(Base):
    __tablename__ = "Manufacturers"
    __table_args__ = {'extend_existing': True} 
    # name
    pass

class Stock(Base):
    __tablename__ = "Stock"
    __table_args__ = {'extend_existing': True} 
    # product_id
    # warehouse_id
    # quantity

    pass
