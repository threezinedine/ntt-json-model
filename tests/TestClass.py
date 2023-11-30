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
        BoolProperty(self, False, "_bIsActive")

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

    @property
    def IsActive(self) -> bool:
        return self._bIsActive.GetValue()
    
    @IsActive.setter
    def IsActive(self, bIsActive: bool) -> None:
        self._bIsActive.SetValue(bIsActive) 

class TestModelClass(ModelBase):
    def __init__(self, nScore: int = 4, *args, **kwargs) -> None:
        super().__init__()

        IntegerProperty(self, nScore, "_nScore")
        ModelProperty(self, TestModel(*args, **kwargs), "_mTestModel")

    @property
    def Score(self) -> int:
        return self._nScore.GetValue()

    @Score.setter
    def Score(self, nNewScore: int) -> None:
        self._nScore.SetValue(nNewScore)

    @property
    def TestModel(self) -> TestModel:
        return self._mTestModel.GetValue()


class TestModelListClass(ModelBase):
    def __init__(self, fScore: float = 8.5) -> None:
        super().__init__()

        FloatProperty(self, fScore, "_fScore")
        ModelListProperty(self, [], "_mModels")
        
    @property
    def Score(self) -> float:
        return self._fScore.GetValue()

    @Score.setter
    def Score(self, fNewScore: float) -> None:
        self._fScore.SetValue(fNewScore)

    @property
    def Models(self) -> List[TestModelClass]:
        return self._mModels.GetValue()

ModelBase.mSubModels[TestModel.__name__] = TestModel
ModelBase.mSubModels[TestModelClass.__name__] = TestModelClass
ModelBase.mSubModels[TestModelListClass.__name__] = TestModelListClass