from sqlalchemy.orm import Session
from models import Dimension, Itfcd
from domain.dimension.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Dimension).order_by(Dimension.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Dimension).get(id)
    return _item

def create_item(db: Session, itfcd: Itfcd, create: Create):
    query = Dimension(itfcd=itfcd,
                        itfcd_id=create.itfcd_id,
                        weight=create.weight,
                        page_cnt=create.page_cnt,
                        dim1=create.dim1,
                        dim2=create.dim2,
                        dim3=create.dim3,
                     )
    db.add(query)
    db.commit()

def update_item(db: Session, item: Dimension, update: Update):
    item.itfcd_id=update.itfcd_id,
    item.weight=update.weight,
    item.page_cnt=update.page_cnt,
    item.dim1=update.dim1,
    item.dim2=update.dim2,
    item.dim3=update.dim3,
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Dimension):
    db.delete(item)
    db.commit()