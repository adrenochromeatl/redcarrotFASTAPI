from sqlalchemy import Column, Integer, String, Float, Boolean, UUID
from database import Base


# Счет (в том числе склады)
class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)
    accountParentId = Column(String)
    parentCorporateId = Column(String)
    # Если "type": "INVENTORY_ASSETS" то это склад
    type = Column(String)
    system = Column(Boolean)
    customTransactionsAllowed = Column(Boolean)


# Бухгалтерская категория номенклатуры
class AccountingCategory(Base):
    __tablename__ = "accounting_category"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)


# Класс алкогольной продукции
class AlcoholClass(Base):
    __tablename__ = "alcohol_class"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)


# Группа аллергенов
class AllergenGroup(Base):
    __tablename__ = "allergen_group"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)


# Тип явки сотрудника
class AttendanceType(Base):
    __tablename__ = "attendance_type"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)


# Концепция
class Conception(Base):
    __tablename__ = "conception"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(String)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)


# Тип места приготовления
class CookingPlaceType(Base):
    __tablename__ = "cooking_place_type"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)


# Тип скидки
class DiscountType(Base):
    __tablename__ = "discount_type"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)


# Единица измерения
class MeasureUnit(Base):
    __tablename__ = "measure_unit"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)


# Тип заказа
class OrderType(Base):
    __tablename__ = "order_type"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)
    orderServiceType = Column(String)
    defaultForServiceType = Column(String)


# Тип оплаты
class PaymentType(Base):
    __tablename__ = "payment_type"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)


# Пользовательская категория номенклатуры
class ProductCategory(Base):
    __tablename__ = "product_category"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)



# Шкала размеров
class ProductScale(Base):
    __tablename__ = "product_scale"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)


# Размер продукта
class ProductSize(Base):
    __tablename__ = "product_size"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)


# Тип смены
class ScheduleType(Base):
    __tablename__ = "schedule_type"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)


# Налоговая категория
class TaxCategory(Base):
    __tablename__ = "tax_category"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    deleted = Column(Boolean)
    code = Column(String)
    name = Column(String, index=True)


# Номенклатура
class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    iiko_id = Column(UUID)
    parentId = Column(UUID)
    num = Column(String)
    code = Column(String)
    name = Column(String, index=True)
    productType = Column(String)
    cookingPlaceType = Column(String)   # Связать с таблицей
    mainUnit = Column(String)   # Связать с таблицей
    productCategory = Column(String)
