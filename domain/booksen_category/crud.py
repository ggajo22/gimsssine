from sqlalchemy.orm import Session
from models import Booksen_category
from domain.booksen_category.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Booksen_category).order_by(Booksen_category.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Booksen_category).get(id)
    return _item

def create_item(db: Session, create: Create):
    query = Booksen_category(
                     category_rank=create.category_rank,
                     category_code=create.category_code,
                     category_name=create.category_name,
                     top_category_code=create.top_category_code,
                     )
    db.add(query)
    db.commit()

def update_item(db: Session, item: Booksen_category, update: Update):
    item.category_rank = update.category_rank,
    item.category_code = update.category_code,
    item.category_name = update.category_name,
    item.top_category_code = update.top_category_code,
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Booksen_category):
    db.delete(item)
    db.commit()