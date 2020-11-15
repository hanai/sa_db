from datetime import datetime, timezone
from sqlalchemy import Column, Date, String, DateTime

from .base import Base
from .engines import engine
from .mixin import DictSerializableMixin


class TickerModel(Base, DictSerializableMixin):
    __tablename__ = 'tickers'

    symbol = Column(String, primary_key=True)
    name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    exchange_code = Column(String)
    description = Column(String)

    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime,
                        default=datetime.now(timezone.utc),
                        onupdate=datetime.now(timezone.utc))

    def __repr__(self):
        return "<Ticker(symbol='%s', name='%s', start_date='%s')" % (
            self.symbol, self.name, self.start_date)


TickerModel.__table__.create(engine, checkfirst=True)
