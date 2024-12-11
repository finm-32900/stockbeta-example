"""Functions for loading factor data from Ken French's data library."""

from __future__ import annotations

import warnings
from typing import TYPE_CHECKING

import pandas_datareader.data as web  # type: ignore

if TYPE_CHECKING:
    from datetime import datetime

    import pandas as pd

# Suppress the specific FutureWarning about date_parser
warnings.filterwarnings("ignore", category=FutureWarning, message=".*date_parser.*")


def load_factors(start: str | datetime | None = None, end: str | datetime | None = None) -> pd.DataFrame:
    """
    Load Fama/French 3 Factors (Daily) from Ken French's data library.

    Parameters
    ----------
    start : str or datetime, optional
        Start date of the data. Format: 'YYYY-MM-DD'
    end : str or datetime, optional
        End date of the data. Format: 'YYYY-MM-DD'

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the following columns:
        - Mkt-RF: Excess return on the market
        - SMB: Small Minus Big (size factor)
        - HML: High Minus Low (value factor)
        - RF: Risk-free rate
    """
    ff_factors = web.DataReader("F-F_Research_Data_Factors_Daily", "famafrench", start=start, end=end)

    # The data comes as a dictionary with keys like '1234' for different tables
    # We want the first table which contains the daily factors
    factors_df = ff_factors[0]

    # Convert returns from percentage to decimal
    return factors_df / 100.0
