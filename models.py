from datetime import timedelta
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float, SmallInteger, func
from sqlalchemy.orm import relationship

from database import Base

class BaseMixin:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp(), onupdate=(func.current_timestamp()))

class Itfcd(Base, BaseMixin):
    __tablename__ = 'itfcd'

    itfcd = Column(String(20), nullable=False)

class Complete(Base, BaseMixin):
    '''
    0 : 처음 상태
    1 : 에러로 실패
    10 : 정상
    -1 : 판매불가
    '''
    __tablename__ = 'complete'

    itfcd_id = Column(Integer, ForeignKey('itfcd.id'))
    is_booksen = Column(Integer, nullable=True)
    is_product = Column(Integer, nullable=True)
    is_image = Column(Integer, nullable=True)
    is_weight = Column(Integer, nullable=True)
    is_price = Column(Integer, nullable=True)
    is_stock = Column(Integer, nullable=True)
    is_variant = Column(Integer, nullable=True)
    itfcd = relationship('Itfcd', backref='completes')

class Failure(Base, BaseMixin):
    __tablename__ = 'failure'

    itfcd_id = Column(Integer, ForeignKey('itfcd.id'))
    section = Column(String(20), nullable=False)
    log = Column(Text, nullable=False)
    itfcd = relationship('Itfcd', backref='failures')

class Booksen_info(Base, BaseMixin):
    __tablename__ = 'booksen_info'

    itfcd_id = Column(Integer, ForeignKey('itfcd.id'))
    is_recent = Column(SmallInteger, nullable=False)
    status = Column(String(10), nullable=False)
    price_sale = Column(Float, nullable=False)
    name = Column(String(100), nullable=False)
    useruse1 = Column(String(30), nullable=False)
    useruse2 = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    opndate = Column(String(10))
    outrt2 = Column(Integer)
    qty = Column(Integer)
    retyn = Column(String(2))
    cover_image_url = Column(Text)
    cover_image_url2 = Column(Text)
    desc_table = Column(Text)
    desc_pub = Column(Text)
    booxen_cate_cd1 = Column(Integer)
    booxen_cate_cd2 = Column(Integer)
    booxen_cate_cd3 = Column(Integer)
    itfcd = relationship('Itfcd', backref='booksen_infos')

class Booksen_category(Base, BaseMixin):
    '''
    category_rank
    특대(베스트셀러, 신간) : 1
    대 : 2
    중 : 3
    소 : 4
    '''
    __tablename__ = 'booksen_category'

    category_rank = Column(SmallInteger, nullable=False)
    category_code = Column(Integer, nullable=False)
    category_name = Column(String(30), nullable=False)
    top_category_code = Column(Integer)

class Writer(Base, BaseMixin):
    __tablename__ = 'writer'

    itfcd_id = Column(Integer, ForeignKey('itfcd.id'))
    name = Column(String(50), nullable=False)
    description = Column(Text)
    is_recent = Column(SmallInteger, nullable=False)
    itfcd = relationship('Itfcd', backref='writers')

class Dimension(Base, BaseMixin):
    __tablename__ = 'dimension'

    itfcd_id = Column(Integer, ForeignKey('itfcd.id'))
    weight = Column(Float, nullable=False)
    page_cnt = Column(Integer, nullable=False)
    dim1 = Column(Float, nullable=False)
    dim2 = Column(Float, nullable=False)
    dim3 = Column(Float, nullable=False)
    itfcd = relationship('Itfcd', backref='dimension')

class Dimension_from(Base, BaseMixin):
    __tablename__ = 'dimension_from'

    itfcd_id = Column(Integer, ForeignKey('itfcd.id'))
    from_data = Column(String(30), nullable=False)
    url = Column(Text, nullable=False)
    itfcd = relationship('Itfcd', backref='dimension_froms')

class Currency(Base, BaseMixin):
    __tablename__ = 'currency'

    nation_code = Column(String(2), nullable=False)
    currency = Column(Float, nullable=False)

class Shopify_product(Base, BaseMixin):
    __tablename__ = 'shopify_product'

    itfcd_id = Column(Integer, ForeignKey('itfcd.id'))
    product_id = Column(Integer, nullable=False)
    itfcd = relationship('Itfcd', backref='shopify_products')

class Shopify_variant(Base, BaseMixin):
    __tablename__ = 'shopify_variant'

    shopify_product_id = Column(Integer, ForeignKey('shopify_product.id'))
    variant_id = Column(Integer, nullable=False)
    inventory_item_id = Column(Integer, nullable=False)
    shopify_product = relationship('Shopify_product', backref='shopify_variants')

class Shopify_image(Base, BaseMixin):
    __tablename__ = 'shopify_image'

    shopify_product_id = Column(Integer, ForeignKey('shopify_product.id'))
    image_id = Column(Integer, nullable=False)
    position = Column(SmallInteger, nullable=False)
    shopify_product = relationship('Shopify_product', backref='shopify_images')

class Shopify_collection(Base, BaseMixin):
    __tablename__ = 'shopify_collection'
    
    booksen_category_id = Column(Integer, ForeignKey('booksen_category.id'))
    collection_id = Column(Integer, nullable=False)
    collection_name = Column(String(30), nullable=False)
    booksen_category = relationship('Booksen_category', backref='shopify_collections')

class Shopify_collect(Base, BaseMixin):
    __tablename__ = 'shopify_collect'

    shopify_product_id = Column(Integer, ForeignKey('shopify_product.id'))
    shopify_collection_id = Column(Integer, ForeignKey('shopify_collection.id'))
    collect_id = Column(Integer, nullable=False)
    shopify_product = relationship('Shopify_product', backref='shopify_collects')
    shopify_collection = relationship('Shopify_collection', backref='shopify_collects')

class Shopify_price(Base, BaseMixin):
    __tablename__ = 'shopify_price'

    shopify_variant_id = Column(Integer, ForeignKey('shopify_variant.id'))
    sales_price = Column(Float, nullable=False)
    shopify_variant = relationship('Shopify_variant', backref='shopify_prices')