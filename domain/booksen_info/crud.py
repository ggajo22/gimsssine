from sqlalchemy.orm import Session
from models import Booksen_info, Itfcd
from domain.booksen_info.schema import Create, Update

def get_items(db: Session):
    _items = db.query(Booksen_info).order_by(Booksen_info.id.asc()).all()
    return _items

def get_item(db: Session, id: int):
    _item = db.query(Booksen_info).get(id)
    return _item

def create_item(db: Session, itfcd: Itfcd, create: Create):
    query = Booksen_info(itfcd=itfcd,
                        itfcd_id=create.itfcd_id,
                        status=create.status,
                        price_sale=create.price_sale,
                        name=create.name,
                        useruse1=create.useruse1,
                        useruse2=create.useruse2,
                        price=create.price,
                        opndate=create.opndate,
                        outrt2=create.outrt2,
                        qty=create.qty,
                        retyn=create.retyn,
                        cover_image_url=create.cover_image_url,
                        cover_image_url2=create.cover_image_url2,
                        desc_table=create.desc_table,
                        desc_pub=create.desc_pub,
                        booxen_cate_cd1=create.booxen_cate_cd1,
                        booxen_cate_cd2=create.booxen_cate_cd2,
                        booxen_cate_cd3=create.booxen_cate_cd3,
                     )
    db.add(query)
    db.commit()

def update_item(db: Session, item: Booksen_info, update: Update):
    item.itfcd_id=update.itfcd_id,
    item.status=update.status,
    item.price_sale=update.price_sale,
    item.name=update.name,
    item.useruse1=update.useruse1,
    item.useruse2=update.useruse2,
    item.price=update.price,
    item.opndate=update.opndate,
    item.outrt2=update.outrt2,
    item.qty=update.qty,
    item.retyn=update.retyn,
    item.cover_image_url=update.cover_image_url,
    item.cover_image_url2=update.cover_image_url2,
    item.desc_table=update.desc_table,
    item.desc_pub=update.desc_pub,
    item.booxen_cate_cd1=update.booxen_cate_cd1,
    item.booxen_cate_cd2=update.booxen_cate_cd2,
    item.booxen_cate_cd3=update.booxen_cate_cd3,
    db.add(item)
    db.commit()

def delete_item(db: Session, item: Booksen_info):
    db.delete(item)
    db.commit()