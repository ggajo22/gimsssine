from sqlalchemy.orm import Session
from models import Failure, Itfcd
from domain.failure.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Failure).order_by(Failure.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Failure).get(id)
    return _item

def create_item(db: Session, itfcd: Itfcd, create: Create):
    query = Failure(itfcd=itfcd,
                        itfcd_id=create.itfcd_id,
                        section=create.section,
                        log=create.log,
                     )
    db.add(query)
    db.commit()

def update_item(db: Session, item: Failure, update: Update):
    item.itfcd_id=update.itfcd_id,
    item.section=update.section,
    item.log=update.log,
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Failure):
    db.delete(item)
    db.commit()