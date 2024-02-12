import random as rn
from enum import Enum

import matplotlib.image as mpimg
from PIL import Image

image_path = "noise_map_001.png"
image = mpimg.imread(image_path)
print(image)

img = Image.open(image_path)

max_colors = 10000

image_colours = img.getcolors(max_colors)
terrain = []

class colourwords(Enum):
  OCEAN = 1
  SHALLOWS = 2
  BEACH = 3
  SCORCHED = 4
  BARE = 5
  TUNDRA = 6
  TEMPERATE_DESERT = 7
  SHRUBLAND = 8
  GRASSLAND = 9
  TEMPERATE_DECIDUOUS_FOREST = 10
  TEMPERATE_RAIN_FOREST = 11
  SUBTROPICAL_DESERT = 12
  TROPICAL_SEASONAL_FOREST = 13
  TROPICAL_RAIN_FOREST = 14
  SNOW = 15
  TAIGA = 16
  SWAMP = 17

class terrainwords(Enum):
  #Trees
  OAK_TREE = 1
  JUNGLE_TREE = 2
  SPRUCE_TREE = 3
  BIRCH_TREE = 4
  BAOBOB = 5
  MUSHROOMS = 6
  BUSH = 7
  FLOWERS = 8
  SMALL_ROCK = 9
  LARGE_ROCK = 10
  POND = 11
  GEYSER = 12
  WATERFALL = 13
  #underwater
  CORAL = 14
  REEF = 15
  ANEMONE = 16

image_biomes = []
if image_colours == (54, 62, 150):
  image_biomes.append(colourwords.OCEAN)
elif image_colours == (88, 205, 237):
  image_biomes.append(colourwords.SHALLOWS)
elif image_colours == (247, 247, 119):
  image_biomes.append(colourwords.BEACH)
elif image_colours == (247, 149, 119):
  image_biomes.append(colourwords.SCORCHED)
elif image_colours == (168, 166, 165):
  image_biomes.append(colourwords.BARE)
elif image_colours == (132, 173, 158):
  image_biomes.append(colourwords.TUNDRA)
elif image_colours == (227, 155, 0):
  image_biomes.append(colourwords.TEMPERATE_DESERT)
elif image_colours == (62, 110, 58):
  image_biomes.append(colourwords.SHRUBLAND)
elif image_colours == (55, 181, 43):
  image_biomes.append(colourwords.GRASSLAND)
elif image_colours == (62, 138, 55):
  image_biomes.append(colourwords.TEMPERATE_DECIDUOUS_FOREST)
elif image_colours == (161, 38, 255):
  image_biomes.append(colourwords.TEMPERATE_RAIN_FOREST)
elif image_colours == (255, 214, 153):
  image_biomes.append(colourwords.SUBTROPICAL_DESERT)
elif image_colours == (102, 153, 0):
  image_biomes.append(colourwords.TROPICAL_SEASONAL_FOREST)
elif image_colours == (255, 0, 119):
  image_biomes.append(colourwords.TROPICAL_RAIN_FOREST)
elif image_colours == (255, 255, 255):
  image_biomes.append(colourwords.SNOW)
elif image_colours == (62, 87, 71):
  image_biomes.append(colourwords.TAIGA)
elif image_colours == (92, 112, 104):
  image_biomes.append(colourwords.SWAMP)


def place_trees():
  def place_oak_tree(image_biomes):
    for i in range(len(image_biomes)):
      if terrain[i] is not None:
        
        match image_biomes:
          case colourwords.GRASSLAND:
            treechance = rn.randint(1, 100)
            if treechance == 1:
              terrain.append(terrainwords.OAK_TREE)
            else:
              terrain.append(None)
  
          case colourwords.TEMPERATE_DECIDUOUS_FOREST:
            treechance = rn.randint(1, 4)
            if treechance == 1:
              terrain.append(terrainwords.OAK_TREE)
            else:
              terrain.append(None)
  def place_jungle_tree(image_biomes):
    for i in range(len(image_biomes)):
      if terrain[i] is not None:
        match image_biomes:
          case colourwords.TROPICAL_SEASONAL_FOREST:
            treechance = rn.randint(1, 7)
            if treechance == 1:
              terrain.append(terrainwords.JUNGLE_TREE)
