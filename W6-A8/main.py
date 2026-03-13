# -----------------------------------------------------------------------------
# main.py.py
# Author: Roxanne Prajapati
# Description:
#      Application entry point.
# -----------------------------------------------------------------------------
from logger import get_logger
from cli_app import CurrencyExchangeCLI
from exchange_rate_service import ExchangeService


def main():
    '''
    Start the application.
    '''
    logger = get_logger()
    service = ExchangeService()
    app = CurrencyExchangeCLI(service, logger)
    app.run()


if __name__ == '__main__':
    main()

