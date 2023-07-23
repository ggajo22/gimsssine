from sqlalchemy.orm import Session
from models import Shopify_image, Shopify_product
from domain.shopify_image.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Shopify_image).order_by(Shopify_image.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Shopify_image).get(id)
    return _item

def create_item(db: Session, shopify_product: Shopify_product, create: Create):
    query = Shopify_image(shopify_product=shopify_product,
                        shopify_product_id=create.shopify_product_id,
                        image_id=create.image_id,
                        position=create.position,
                     )
    db.add(query)
    db.commit()

def update_item(db: Session, item: Shopify_image, update: Update):
    item.shopify_product_id=update.shopify_product_id,
    item.image_id=update.image_id,
    item.position=update.position,
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Shopify_image):
    db.delete(item)
    db.commit()