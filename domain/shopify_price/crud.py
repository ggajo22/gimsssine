from sqlalchemy.orm import Session
from models import Shopify_price, Shopify_variant
from domain.shopify_price.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Shopify_price).order_by(Shopify_price.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Shopify_price).get(id)
    return _item

def create_item(db: Session, shopify_variant: Shopify_variant, create: Create):
    query = Shopify_price(shopify_variant=shopify_variant,
                        shopify_variant_id=create.shopify_variant_id,
                        sales_price=create.sales_price,
                     )
    db.add(query)
    db.commit()

def update_item(db: Session, item: Shopify_price, update: Update):
    item.shopify_variant_id=update.shopify_variant_id,
    item.sales_price=update.sales_price,
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Shopify_price):
    db.delete(item)
    db.commit()