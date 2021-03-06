class TcspcError(Exception):
    """Base class for TCSPC-Fit errors."""

###
# region: IO errors
###

class TcspcIoError(TcspcError):
    """Base class for IO related errors."""

class UnknownBrand(TcspcIoError):
    """Unknown brand for data file."""

class UnknownModel(TcspcIoError):
    """Unknown model for the specified manufacturer."""
###
# endregion
###