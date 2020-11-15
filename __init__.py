from sqlalchemy.orm import sessionmaker

from .base import Base
from .daily_price import get_daily_price_model
from .engines import engine
from .ticker import TickerModel

TickerSession = sessionmaker(bind=engine)
DailyPriceSession = sessionmaker(bind=engine)
