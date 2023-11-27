from typing import *
from ntt_signal import Signal
from .Exception import *


class ModelBase(Signal):
    def __init__(self) -> None:
        super().__init__()
        self._strDataAttributeNames: List[str] = []

    def _AppendModelData(self, strAttributeName: str) -> None:
        self._strDataAttributeNames.append(strAttributeName)

    def ToDict(self) -> dict:
        dictData: dict = {}

        for strAttributeName in self._strDataAttributeNames:
            dictData[strAttributeName] = getattr(self, strAttributeName).GetValue()

        dictData["__class__"] = self.__class__.__name__

        return dictData

    def FromDict(self, dictData: dict) -> None:
        if "__class__" not in dictData:
            raise InputDictError("Input dict has no __class__ key")
        elif dictData["__class__"] != self.__class__.__name__:
            raise TargetClassError(f"Expect {self.__class__.__name__} but received {dictData['__class__']}")
        else:
            for strAttributeName in self._strDataAttributeNames:
                if strAttributeName in dictData:
                    getattr(self,strAttributeName).SetValue(dictData[strAttributeName], False)
            self.Emit()