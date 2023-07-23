from sqlalchemy.orm import Session
from models import Writer, Itfcd
from domain.writer.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Writer).order_by(Writer.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Writer).get(id)
    return _item

def create_item(db: Session, itfcd: Itfcd, create: Create):
    query = Writer(itfcd=itfcd,
                        itfcd_id=create.itfcd_id,
                        name=create.name,
                        description=create.description,
                        is_recent=create.is_recent,
                     )
    db.add(query)
    db.commit()

def update_item(db: Session, item: Writer, update: Update):
    item.itfcd_id=update.itfcd_id,
    item.name=update.name,
    item.description=update.description,
    item.is_recent=update.is_recent,
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Writer):
    db.delete(item)
    db.commit()