import converters
from converters import kg_to_lbs

result_lbs = kg_to_lbs(100)
print(int(result_lbs))

result_kg = converters.lbs_to_kg(40)
print(result_kg)
