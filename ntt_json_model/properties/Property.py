from typing import *
from abc import *
from ntt_signal import Signal
from ..ModelBase import ModelBase


class Property(Signal, ABC):
    def __init__(self, model:ModelBase, strAttributeName: str, datatype: type = None) -> None:
        super().__init__(datatype)
        self.Attach(model)
        setattr(model, strAttributeName, self)
        model._AppendModelData(strAttributeName)

    @abstractmethod
    def GetValue(self) -> Any:
        pass

    @abstractmethod
    def SetValue(self, newValue: object, bNotify: bool = True) -> None:
        pass