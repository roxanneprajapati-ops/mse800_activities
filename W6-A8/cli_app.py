# -----------------------------------------------------------------------------
# cli_app.py - Command-line interface layer.
# Author: Roxanne Prajapati
# Description:
#      Handles all user interaction via the command line.
# -----------------------------------------------------------------------------

from exchange_rate_service import ExchangeService, ValidationError
from database_manager import DatabaseManager, DatabaseError


class CurrencyExchangeCLI:
    def __init__(self, service: ExchangeService, logger):
        '''
        Create the CLI instance.

        :param service: ExchangeService instance.
        :param logger: Logger instance.
        '''
        self._service = service
        self._logger = logger

    def run(self):
        '''
        Start the CLI loop.
        '''
        DatabaseManager().init_schema()
        self._logger.info('Application started.')

        while True:
            print('\n=== Currency Exchange CLI ===')
            print('1) View current exchange rate')
            print('2) Update exchange rate')
            print('3) Convert amount')
            print('0) Exit')

            choice = input('Choose: ').strip()

            try:
                if choice == '1':
                    self._show_rate()
                elif choice == '2':
                    self._update_rate()
                elif choice == '3':
                    self._convert_amount()
                elif choice == '0':
                    self._logger.info('Application exited by user.')
                    print('Goodbye!')
                    break
                else:
                    print('Invalid choice. Please select 0–3.')

            except ValidationError as exc:
                self._logger.warning('Validation error: %s', exc)
                print(f'Input error: {exc}')

            except DatabaseError as exc:
                self._logger.error('Database error: %s', exc)
                print(f'Database error: {exc}')

            except Exception as exc:
                self._logger.exception('Unexpected error: %s', exc)
                print('Unexpected error occurred. Check logs/app.log for details.')

    def _show_rate(self):
        '''
        Display the current exchange rate.
        '''
        rate = self._service.get_current_rate()
        print(f'Current rate: 1 {rate.base_currency} = {rate.rate} {rate.target_currency}')
        print(f'Last updated (UTC): {rate.updated_at}')

    def _update_rate(self):
        '''
        Prompt user and update the exchange rate.
        '''
        base = input('Base currency (e.g., NZD): ').strip()
        target = input('Target currency (e.g., USD): ').strip()
        rate = input('Exchange rate (e.g., 0.60): ').strip()

        updated = self._service.set_rate(base, target, rate)
        print(f'Updated rate: 1 {updated.base_currency} = {updated.rate} {updated.target_currency}')

    def _convert_amount(self):
        '''
        Prompt user and convert an amount.
        '''
        amount = input('Amount to convert: ').strip()
        current = self._service.get_current_rate()
        conversion = self._service.convert(amount)

        print(f'{conversion.amount} {current.base_currency} = {conversion.converted_amount} {current.target_currency}')
        print(f'Conversion time (UTC): {conversion.timestamp}')
