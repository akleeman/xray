from .core.alignment import align
from .core.variable import Variable, Coordinate
from .core.dataset import Dataset, open_dataset
from .core.dataarray import DataArray

from .version import version as __version__

# TODO: define a global "concat" function to provide a uniform interface
