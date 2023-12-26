from lib.roundRegionName import roundRegionName

def getRegionFilesFromCoordinates(cornerOne: list[int], cornerTwo: list[int]) -> list[str]:
  [lowestX, lowestZ] = cornerOne
  [highestX, highestZ] = cornerTwo

  bottomLeftRegion = [roundRegionName(lowestX), roundRegionName(lowestZ)]
  topRightRegion = [roundRegionName(highestX), roundRegionName(highestZ)]

  allRegionFiles = []
  for x in range(bottomLeftRegion[0], (topRightRegion[0] + 1) ):
    for z in range(bottomLeftRegion[1], (topRightRegion[1] + 1 )):
      allRegionFiles.append(f"r.{x}.{z}.mca")
  
  return allRegionFiles
  
