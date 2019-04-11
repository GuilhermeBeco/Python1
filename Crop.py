class Crop:
    def __init__(self,growthRate,lightNeed,watterNeed):
        self._growth=0
        self._daysToGrowth=0
        self._growthRate=growthRate
        self._lightNeed=lightNeed
        self._watterNeed=watterNeed
        self._status="Seed"
        self._type="Generic"
