import sys
# Add a new directory path to import new modules
sys.path.append('e:\\Lavid')

from importable import findItem
import importable2
import random


gary = ['meow', 'planckton', 'spongeBob', 'Patrick']

print(findItem('Patrick', gary))
print(importable2.wooof())
print(sys.path)
randomItem = random.choice(gary)
print(randomItem)