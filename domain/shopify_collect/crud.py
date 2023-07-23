from sqlalchemy.orm import Session
from models import Shopify_collect, Shopify_product, Shopify_collection
from domain.shopify_collect.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Shopify_collect).order_by(Shopify_collect.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Shopify_collect).get(id)
    return _item

def create_item(db: Session, shopify_product: Shopify_product, shopify_collection: Shopify_collection, create: Create):
    query = Shopify_collect(shopify_product=shopify_product,
                        shopify_collection=shopify_collection,
                        shopify_product_id=create.shopify_product_id,
                        shopify_collection_id=create.shopify_collection_id,
                        collect_id=create.collect_id,
                     )
    db.add(query)
    db.commit()

def update_item(db: Session, item: Shopify_collect, update: Update):
    item.shopify_product_id=update.shopify_product_id,
    item.shopify_collection_id=update.shopify_collection_id,
    item.collect_id=update.collect_id,
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Shopify_collect):
    db.delete(item)
    db.commit()