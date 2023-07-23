from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.shopify_price import schema, crud
from domain.shopify_variant import crud as shopify_variant_crud

router = APIRouter(
    prefix="/api/shopify/price",
)

@router.get("/", response_model=list[schema.Item])
def get_items(db: Session = Depends(get_db)):
    _items = crud.get_items(db)
    return _items

@router.get("/{id}", response_model=schema.Item)
def get_item(id: int, db: Session = Depends(get_db)):
    _item = crud.get_item(db, id)
    return _item

@router.post("/", status_code=status.HTTP_204_NO_CONTENT)
def create_item(shopify_variant_id: int, create: schema.Create, db: Session = Depends(get_db)):
    shopify_variant = shopify_variant_crud.get_item(db, id=shopify_variant_id)
    if not shopify_variant:
        raise HTTPException(status_code=404, detail="없는 shopify_variant_id 입니다.")
    crud.create_item(db, shopify_variant=shopify_variant, create=create)

@router.put("/", status_code=status.HTTP_204_NO_CONTENT)
def update_item(update: schema.Update, db: Session = Depends(get_db)):
    item = crud.get_item(db, id=update.id)
    if not item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    crud.update_item(db=db, item=item, update=update)

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(delete: schema.Delete, db: Session = Depends(get_db)):
    item = crud.get_item(db, id=delete.id)
    if not item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    crud.delete_item(db=db, item=item)