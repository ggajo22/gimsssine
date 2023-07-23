from sqlalchemy.orm import Session
from models import Currency
from domain.currency.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Currency).order_by(Currency.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Currency).get(id)
    return _item

def create_item(db: Session, create: Create):
    query = Currency(
                     nation_code=create.nation_code,
                     currency=create.currency,
                     )
    db.add(query)
    db.commit()

def update_item(db: Session, item: Currency, update: Update):
    item.nation_code=update.nation_code,
    item.currency=update.currency,
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Currency):
    db.delete(item)
    db.commit()