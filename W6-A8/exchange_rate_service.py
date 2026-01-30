# -----------------------------------------------------------------------------
# exhange_rate_service.py - Exchange Rate Business Logic
# Author: Roxanne Prajapati
# Description:
#      Coordinates currency exchange operations and delegates persistence 
# to DatabaseManager.
# -----------------------------------------------------------------------------
from exchange_rate import ExchangeRate
from conversion import Conversion
from database_manager import DatabaseManager


class ValidationError(ValueError):
    '''
    Raised when input validation fails.
    '''


class ExchangeService:

    def __init__(self):
        '''
        Create the service instance.
        '''
        self._db = DatabaseManager()

    def get_current_rate(self) -> ExchangeRate:
        '''
        Return the current exchange rate.

        :return: ExchangeRate instance.
        '''
        return self._db.get_rate()

    def set_rate(self, base: str, target: str, rate_value) -> ExchangeRate:
        '''
        Update the exchange rate.

        :param base: Base currency code.
        :param target: Target currency code.
        :param rate_value: Exchange rate value.
        :return: Updated ExchangeRate instance.
        '''
        try:
            rate = ExchangeRate(base, target, rate_value, ExchangeRate.now_iso())
        except ValueError as exc:
            raise ValidationError(str(exc)) from exc

        self._db.insert_rate(rate)
        return rate

    def convert(self, amount_value) -> Conversion:
        '''
        Convert an amount using the current exchange rate.

        :param amount_value: Amount to convert.
        :return: Conversion instance.
        '''
        try:
            amount = float(amount_value)
        except (TypeError, ValueError) as exc:
            raise ValidationError('amount must be a number.') from exc

        if amount <= 0:
            raise ValidationError('amount must be greater than 0.')

        rate = self.get_current_rate()
        converted_amount = round(amount * rate.rate, 2)

        try:
            conversion = Conversion(
                amount=amount,
                converted_amount=converted_amount,
                rate_used=rate.rate,
                timestamp=Conversion.now_iso()
            )
        except ValueError as exc:
            raise ValidationError(str(exc)) from exc

        self._db.insert_conversion(conversion)
        return conversion
