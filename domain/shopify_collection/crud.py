from sqlalchemy.orm import Session
from models import Shopify_collection, Booksen_category
from domain.shopify_collection.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Shopify_collection).order_by(Shopify_collection.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Shopify_collection).get(id)
    return _item

def create_item(db: Session, booksen_category: Booksen_category, create: Create):
    query = Shopify_collection(booksen_category=booksen_category,
                        booksen_category_id=create.booksen_category_id,
                        collection_id=create.collection_id,
                        collection_name=create.collection_name,
                     )
    db.add(query)
    db.commit()

def update_item(db: Session, item: Shopify_collection, update: Update):
    item.booksen_category_id=update.booksen_category_id,
    item.collection_id=update.collection_id,
    item.collection_name=update.collection_name,
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Shopify_collection):
    db.delete(item)
    db.commit()