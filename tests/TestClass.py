from ntt_json_model import *


class TestModel(ModelBase):
    def __init__(self, 
                    nValue: int = 3, 
                    strName: str = "Hello",
                    fTemp: float = 3.1,
                    lstScores: List[int] = []) -> None:
        super().__init__()

        IntegerProperty(self, nValue, "_nValue")
        FloatProperty(self, fTemp, "_fTemp")
        StrProperty(self, strName, "_strName")
        ListProperty(self, lstScores, "_lstScores")

    @property
    def Value(self) -> int:
        return self._nValue.GetValue()

    @Value.setter
    def Value(self, nValue: int) -> None:
        self._nValue.SetValue(nValue)

    @property
    def Temp(self) -> str:
        return self._fTemp.GetValue()

    @Temp.setter
    def Temp(self, fTemp: float) -> None:
        self._fTemp.SetValue(fTemp)
    
    @property
    def Name(self) -> str:
        return self._strName.GetValue()

    @Name.setter
    def Name(self, strName: str) -> None:
        self._strName.SetValue(strName)

    @property
    def Scores(self) -> List[int]:
        return self._lstScores.GetValue()