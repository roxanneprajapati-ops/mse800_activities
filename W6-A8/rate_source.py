# -----------------------------------------------------------------------------
# rate_source.py Abstract rate source definition
# Author: Roxanne Prajapati
# Description:
#      Abstract base class for retrieving exchange rates.
# -----------------------------------------------------------------------------
from abc import ABC, abstractmethod
from exchange_rate import ExchangeRate


class RateSource(ABC):
    '''
    Abstract base class for retrieving exchange rates.
    '''

    @abstractmethod
    def get_rate(self) -> ExchangeRate:
        '''
        Return the current exchange rate.

        :return: ExchangeRate instance.
        '''
        pass
