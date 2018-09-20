# PerformanceUtils
# formulas.py
# Copyright (c) 2018 Performance Analytics
# License: MIT
 

from abc import ABC, abstractmethod
import math

import datatypes as T


class Formula(ABC):

    @staticmethod
    @abstractmethod
    def load(reps: T.Quantity, max: T.Load) -> T.Load:
        pass
    
    @staticmethod
    @abstractmethod
    def max(reps: T.Quantity, load: T.Load) -> T.Load:
        pass
    
    @staticmethod
    @abstractmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        pass


class Brzycki(Formula):

    @staticmethod
    def load(reps: T.Quantity, max: T.Load) -> T.Load:
        return max * (37 - reps) / 36
    
    @staticmethod
    def max(reps: T.Quantity, load: T.Load) -> T.Load:
        return load * 36 / (37 - reps)

    @staticmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        return 37 - intensity * 36


class Epley(Formula):

    @staticmethod
    def load(reps: T.Quantity, max: T.Load) -> T.Load:
        return max / (1 + reps / 30)
    
    @staticmethod
    def max(reps: T.Quantity, load: T.Load) -> T.Load:
        return load * (1 + reps / 30)

    @staticmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        return 30 * (1 / intensity - 1)


class McGlothin(Formula):

    @staticmethod
    def load(reps: T.Quantity, max: T.Load) -> T.Load:
        return max * (101.3 - 2.67123 * reps) / 100
    
    @staticmethod
    def max(reps: T.Quantity, load: T.Load) -> T.Load:
        return 100 * load / (101.3 - 2.67123 * reps)

    @staticmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        return (101.3 - 100 * intensity) / 2.67123


class Lombardi(Formula):

    @staticmethod
    def load(reps: T.Quantity, max: T.Load) -> T.Load:
        return max / (reps ** 0.1)
    
    @staticmethod
    def max(reps: T.Quantity, load: T.Load) -> T.Load:
        return reps ** 0.1 * load

    @staticmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        return intensity ** -10


class Mayhew(Formula):

    @staticmethod
    def load(reps: T.Quantity, max: T.Load) -> T.Load:
        return max * (52.2 + 41.9 * (math.e ** (-0.055 * reps))) / 100
    
    @staticmethod
    def max(reps: T.Quantity, load: T.Load) -> T.Load:
        return 100 * load / (52.2 + 41.9 * (math.e ** (-0.055 * reps)))

    @staticmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        return 200 / 11 * math.log(419 / (2 * (500 * intensity - 261)))


class OConner(Formula):

    @staticmethod
    def load(reps: T.Quantity, max: T.Load) -> T.Load:
        return max / (1 + reps / 40)
    
    @staticmethod
    def max(reps: T.Quantity, load: T.Load) -> T.Load:
        return load * (1 + reps / 40)

    @staticmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        return 40 * (1 / intensity - 1)


class Wathan(Formula):

    @staticmethod
    def load(reps: T.Quantity, max: T.Load) -> T.Load:
        return max * (48.8 + 53.8 * (math.e ** (-0.075 * reps))) / 100
    
    @staticmethod
    def max(reps: T.Quantity, load: T.Load) -> T.Load:
        return 100 * load / (48.8 + 53.8 * (math.e ** (-0.075 * reps)))

    @staticmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        return 40 / 3 * math.log(269 / (500 * intensity - 244))