from datetime import datetime, timezone
from sqlalchemy import Column, Date, Float, Integer, DateTime

from .base import Base
from .engines import engine

model_cache = dict()


def create_daily_price_model(symbol: str):
    Model = type(
        "DailyPriceModel_%s" % symbol,
        (Base, ),
        dict(__tablename__='dp_' + symbol.lower(),
             date=Column(Date, primary_key=True),
             open=Column(Float),
             high=Column(Float),
             low=Column(Float),
             close=Column(Float),
             adj_open=Column(Float),
             adj_high=Column(Float),
             adj_low=Column(Float),
             adj_close=Column(Float),
             volume=Column(Integer),
             adj_volume=Column(Integer),
             split_factor=Column(Float),
             created_at=Column(DateTime, default=datetime.now(timezone.utc)),
             updated_at=Column(DateTime,
                               default=datetime.now(timezone.utc),
                               onupdate=datetime.now(timezone.utc))),
    )

    Model.__table__.create(engine, checkfirst=True)

    return Model


def get_daily_price_model(symbol: str):
    if symbol in model_cache:
        return model_cache[symbol]
    else:
        model = create_daily_price_model(symbol)
        model_cache[symbol] = model
        return model
