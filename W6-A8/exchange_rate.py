# -----------------------------------------------------------------------------
# exchange_rate.py ExchangeRate domain model.
# Author: Roxanne Prajapati
# Description:
#      ExchangeRate domain model demonstrating encapsulation using protected 
# attributes and properties with validation.
# -----------------------------------------------------------------------------
from datetime import datetime


'''
exchange_rate.py
ExchangeRate domain model.
'''

from datetime import datetime


class ExchangeRate:
    '''
    Represents a single exchange rate from a base currency to a target currency.
    Encapsulation is enforced via protected attributes and property setters.
    '''

    def __init__(self, base_currency: str, target_currency: str, rate, updated_at: str) -> None:
        '''
        Create an ExchangeRate instance.

        :param base_currency: Base currency code (e.g., NZD).
        :param target_currency: Target currency code (e.g., USD).
        :param rate: Exchange rate value (> 0).
        :param updated_at: ISO timestamp string.
        '''
        self._base_currency = None
        self._target_currency = None
        self._rate = None
        self._updated_at = updated_at

        # Use setters so validation is applied at creation time
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.rate = rate

    @staticmethod
    def now_iso() -> str:
        '''
        Return the current UTC timestamp in ISO format.

        :return: ISO formatted timestamp string.
        '''
        return datetime.utcnow().isoformat(timespec='seconds')

    @property
    def base_currency(self) -> str:
        '''
        Return the base currency code.

        :return: Base currency code.
        '''
        return self._base_currency

    @base_currency.setter
    def base_currency(self, value: str) -> None:
        cleaned = value.strip().upper()
        if not cleaned.isalpha() or len(cleaned) != 3:
            raise ValueError('base_currency must be a 3-letter code (e.g., NZD).')
        self._base_currency = cleaned

    @property
    def target_currency(self) -> str:
        '''
        Return the target currency code.

        :return: Target currency code.
        '''
        return self._target_currency

    @target_currency.setter
    def target_currency(self, value: str) -> None:
        cleaned = value.strip().upper()
        if not cleaned.isalpha() or len(cleaned) != 3:
            raise ValueError('target_currency must be a 3-letter code (e.g., USD).')
        self._target_currency = cleaned

    @property
    def rate(self) -> float:
        '''
        Return the exchange rate value.

        :return: Exchange rate value.
        '''
        return self._rate

    @rate.setter
    def rate(self, value) -> None:
        try:
            rate = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError('rate must be a number.') from exc

        if rate <= 0:
            raise ValueError('rate must be greater than 0.')
        self._rate = rate

    @property
    def updated_at(self) -> str:
        '''
        Return the last updated timestamp.

        :return: Timestamp string.
        '''
        return self._updated_at
