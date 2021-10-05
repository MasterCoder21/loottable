"""
MIT License

Copyright (c) 2021 minecraftpr03

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import random
from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Union
import json


class LootTable(ABC):
  @abstractmethod
  def pick(self):
    pass

  @abstractmethod
  def additem(self, item: Any, weight: int):
    pass

  @abstractmethod
  def delitem(self, index: int):
    pass

class WeightedLootTable(LootTable):
  def __init__(self, keys: List[Union[Tuple, List]] = None):
    if keys:
      self._keys = keys
    else:
      self._keys = []

  def pick(self):
    if len(self._keys) == 0:
      raise KeyError("Keys length is 0, cannot pick item from empty list")
    
    choices = []

    for item, weight in self._keys:
      choices.extend([item]*weight)

    return random.choice(choices)

  def additem(self, item: Any, weight: int):
    self._keys.append((item, weight))

  @classmethod
  def from_file(cls, fp: str):
    data = json.load(open(fp))

    if type(data) != list:
      raise ValueError("JSON data of provided file path was not stored in list format")

    if len(data) == 0:
      raise ValueError("Length of JSON data is 0, provide a JSON list with a length greater than or equal to 1")

    itemIndex = 0

    try:
      for a, b in data:
        itemIndex += 1
    except:
      raise KeyError("Object at list index %s was not a tuple in the format (item, weight)" % itemIndex)

    return cls(data)

  def delitem(self, index: int):
    return self._keys.pop(index)

  def pickmany(self, amount: int):
    for i in range(amount):
      yield self.pick()

  def save(self, fp: str):
    with open(fp, "w") as f:
      json.dump(self._keys, f)

  @property
  def keys(self):
    return self._keys

#  Add more subclassed loot tables here!