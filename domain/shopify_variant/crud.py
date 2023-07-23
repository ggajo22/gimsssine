from sqlalchemy.orm import Session
from models import Shopify_variant, Shopify_product
from domain.shopify_variant.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Shopify_variant).order_by(Shopify_variant.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Shopify_variant).get(id)
    return _item

def create_item(db: Session, shopify_product: Shopify_product, create: Create):
    query = Shopify_variant(shopify_product=shopify_product,
                        shopify_product_id=create.shopify_product_id,
                        variant_id=create.variant_id,
                        inventory_item_id=create.inventory_item_id,
                     )
    db.add(query)
    db.commit()

def update_item(db: Session, item: Shopify_variant, update: Update):
    item.shopify_product_id=update.shopify_product_id,
    item.variant_id=update.variant_id,
    item.inventory_item_id=update.inventory_item_id,
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Shopify_variant):
    db.delete(item)
    db.commit()