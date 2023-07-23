from sqlalchemy.orm import Session
from models import Shopify_product, Itfcd
from domain.shopify_product.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Shopify_product).order_by(Shopify_product.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Shopify_product).get(id)
    return _item

def create_item(db: Session, itfcd: Itfcd, create: Create):
    query = Shopify_product(itfcd=itfcd,
                        itfcd_id=create.itfcd_id,
                        product_id=create.product_id,
                     )
    db.add(query)
    db.commit()

def update_item(db: Session, item: Shopify_product, update: Update):
    item.itfcd_id=update.itfcd_id,
    item.product_id=update.product_id,
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Shopify_product):
    db.delete(item)
    db.commit()