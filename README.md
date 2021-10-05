# loottable
### A simple Python library for making loot tables from JSON files and Python dictionaries

---

Installing from git (with pip):

`$ pip install git+https://github.com/MasterCoder21/loottable.git
`

---
### Classes
#### LootTable
 - Extends: `abc.ABC`
 - Abstract class
 - Methods to override:
   - pick()
    ```py
    @abstractmethod
    def additem(self, item: Any, weight: int):
      pass
    ```
   - additem()
    ```py
    @abstractmethod
    def additem(self, item: Any, weight: int):
      pass
   - delitem()
    ```py
    @abstractmethod
    def delitem(self, index: int):
      pass
    ```
#### WeightedLootTable
 - Extends: `loottable.LootTable`
 - Constructor:
    ```py
    def __init__(self, keys: List[Union[Tuple, List]] = None):
      if keys:
        self._keys = keys
      else:
        self._keys = []
    ```
 - Methods:
   - pick() - Picks a random weighted item from the instance's data
   - additem() - Add an item with a specific weight
   - delitem() - Delete an item by index
   - save() - Save the instance's data to a JSON file
 - Generators:
   - pickmany() - Yields a certain amount of random weighted items
 - Class methods:
   - from_file() - Creates a new instance with pre-made data from a JSON file
 - Properties:
   - keys - Getter only; no setter

### Example
```py
from loottable import WeightedLootTable

loot = WeightedLootTable([("item1", 15), ("item2", 20), ("item3", 40)])

print("One item picked")
print(loot.pick())

print("\nMultiple items picked")

for item in loot.pickmany(10):
  print(item)

print("Add an item")
loot.additem("item4", 25)

print("Delete an item by index")
loot.delitem(2) # Deletes by list index, not by item number (Deleting index 2 would remove the third item from the list)

print("Get the instance's keys")
print(loot.keys)

print("Save the instance's data to a JSON file")
loot.save("loot.json")

print("Make a new instance from that file")
loot2 = WeightedLootTable.from_file("loot.json")
```
The generic `LootTable` class allows you to make your own loot tables with custom data formats, rules, and randomized pickers.
