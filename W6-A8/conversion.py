# -----------------------------------------------------------------------------
# conversion.py Conversion domain model
# Author: Roxanne Prajapati
# Description:
#      Represents a currency conversion transaction.
# -----------------------------------------------------------------------------
from datetime import datetime

class Conversion:
    '''
    Represents a currency conversion transaction.
    Encapsulation is enforced via protected attributes and property setters.
    '''

    def __init__(self, amount, converted_amount, rate_used, timestamp: str) -> None:
        '''
        Create a Conversion instance.

        :param amount: Original amount (> 0).
        :param converted_amount: Converted amount (> 0).
        :param rate_used: Exchange rate used (> 0).
        :param timestamp: ISO timestamp string.
        :return: None
        '''
        self._amount = None
        self._converted_amount = None
        self._rate_used = None
        self._timestamp = timestamp

        # Apply validation via setters
        self.amount = amount
        self.converted_amount = converted_amount
        self.rate_used = rate_used

    @staticmethod
    def now_iso() -> str:
        '''
        Return the current UTC timestamp in ISO format.

        :return: ISO formatted timestamp string.
        '''
        return datetime.utcnow().isoformat(timespec='seconds')

    @property
    def amount(self) -> float:
        '''
        Return the original amount.

        :return: Amount value.
        '''
        return self._amount

    @amount.setter
    def amount(self, value) -> None:
        self._amount = self._validate_positive(value, 'amount')

    @property
    def converted_amount(self) -> float:
        '''
        Return the converted amount.

        :return: Converted amount.
        '''
        return self._converted_amount

    @converted_amount.setter
    def converted_amount(self, value) -> None:
        self._converted_amount = self._validate_positive(value, 'converted_amount')

    @property
    def rate_used(self) -> float:
        '''
        Return the exchange rate used.

        :return: Rate used.
        '''
        return self._rate_used

    @rate_used.setter
    def rate_used(self, value) -> None:
        self._rate_used = self._validate_positive(value, 'rate_used')

    @property
    def timestamp(self) -> str:
        '''
        Return the conversion timestamp.

        :return: Timestamp string.
        '''
        return self._timestamp

    def _validate_positive(self, value, field_name: str) -> float:
        '''
        Validate that a value is numeric and greater than zero.

        :param value: Value to validate.
        :param field_name: Name used for error messages.
        :return: Validated float value.
        '''
        try:
            number = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f'{field_name} must be a number.') from exc

        if number <= 0:
            raise ValueError(f'{field_name} must be greater than 0.')

        return number
