import yaml

excludedRegions = ["__global__", "wprowadzenie"]

def getRegionsFromYaml(yamlFile):
  allRegions = []
  with open(yamlFile, 'r') as file:
    yamlRegions = yaml.safe_load(file)['regions']
    for _, regionName in enumerate(yamlRegions):
      if (regionName in excludedRegions):
        continue
      currentRegion = yamlRegions[regionName]
      regionMinX = currentRegion['min']['x']
      regionMinZ = currentRegion['min']['z']

      regionMaxX = currentRegion['max']['x']
      regionMaxZ = currentRegion['max']['z']

      allRegions.append({
        "name": regionName,
        "min": [regionMinX, regionMinZ],
        "max": [regionMaxX, regionMaxZ], 
        })
  
  return allRegions
