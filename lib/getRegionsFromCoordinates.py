from lib.roundRegionName import roundRegionName

def getRegionsFromCoordinates(cornerOne: list[int], cornerTwo: list[int]) -> list[str]:
  [lowestX, lowestZ] = cornerOne
  [highestX, highestZ] = cornerTwo

  bottomLeftRegion = [roundRegionName(lowestX), roundRegionName(lowestZ)]
  topRightRegion = [roundRegionName(highestX), roundRegionName(highestZ)]

  allRegions = []

  for x in range(bottomLeftRegion[0], (topRightRegion[0] + 1) ):
    for z in range(bottomLeftRegion[1], (topRightRegion[1] + 1 )):
      allRegions.append(f"r.{x}.{z}.mca")
  
  return allRegions
  