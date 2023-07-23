from sqlalchemy.orm import Session
from models import Complete, Itfcd
from domain.complete.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Complete).order_by(Complete.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Complete).get(id)
    return _item

def create_item(db: Session, itfcd: Itfcd, create: Create):
    query = Complete(itfcd=itfcd,
                     itfcd_id=create.itfcd_id,
                     is_booksen=create.is_booksen,
                     is_product=create.is_product,
                     is_image=create.is_image,
                     is_weight=create.is_weight,
                     is_price=create.is_price,
                     is_stock=create.is_stock,
                     is_variant=create.is_variant,
                     )
    db.add(query)
    db.commit()

def update_item(db: Session, item: Complete, update: Update):
    if update.is_booksen > 0:
        item.is_booksen = update.is_booksen
    if update.is_product > 0:
        item.is_product = update.is_product
    if update.is_image > 0:
        item.is_image = update.is_image
    if update.is_weight > 0:
        item.is_weight = update.is_weight
    if update.is_price > 0:
        item.is_price = update.is_price
    if update.is_stock > 0:
        item.is_stock = update.is_stock
    if update.is_variant > 0:
        item.is_variant = update.is_variant
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Complete):
    db.delete(item)
    db.commit()

def get_complete_booksen_items(db: Session, status: int):
    _items = db.query(Complete).filter_by(is_booksen=status).all()
    return _items

def get_complete_product_items(db: Session, status: int):
    _items = db.query(Complete).filter_by(is_product=status).all()
    return _items

def get_complete_image_items(db: Session, status: int):
    _items = db.query(Complete).filter_by(is_image=status).all()
    return _items

def get_complete_weight_items(db: Session, status: int):
    _items = db.query(Complete).filter_by(is_weight=status).all()
    return _items

def get_complete_price_items(db: Session, status: int):
    _items = db.query(Complete).filter_by(is_price=status).all()
    return _items

def get_complete_stock_items(db: Session, status: int):
    _items = db.query(Complete).filter_by(is_stock=status).all()
    return _items

def get_complete_variant_items(db: Session, status: int):
    _items = db.query(Complete).filter_by(is_variant=status).all()
    return _items