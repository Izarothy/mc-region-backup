from math import floor, ceil

def roundRegionName(coordinate: int) -> int:
  if (coordinate < 0):
    if (coordinate >= -512):
      return ceil(coordinate / 512) 
  
  return floor(coordinate / 512)
