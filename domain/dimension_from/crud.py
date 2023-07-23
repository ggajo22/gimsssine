from sqlalchemy.orm import Session
from models import Dimension_from, Itfcd
from domain.dimension_from.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Dimension_from).order_by(Dimension_from.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Dimension_from).get(id)
    return _item

def create_item(db: Session, itfcd: Itfcd, create: Create):
    query = Dimension_from(itfcd=itfcd,
                        itfcd_id=create.itfcd_id,
                        from_data=create.from_data,
                        url=create.url,
                     )
    db.add(query)
    db.commit()

def update_item(db: Session, item: Dimension_from, update: Update):
    item.itfcd_id=update.itfcd_id,
    item.from_data=update.from_data,
    item.url=update.url,
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Dimension_from):
    db.delete(item)
    db.commit()