from sqlalchemy.orm import Session
from models import Itfcd
from domain.itfcd.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Itfcd).order_by(Itfcd.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Itfcd).get(id)
    return _item

def create_item(db: Session, create: Create):
    query = Itfcd(itfcd=create.itfcd)
    db.add(query)
    db.commit()

def update_item(db: Session, item: Itfcd, update: Update):
    item.itfcd = update.itfcd
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Itfcd):
    db.delete(item)
    db.commit()