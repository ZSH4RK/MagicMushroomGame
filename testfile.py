from enum import Enum

import matplotlib.image as mpimg
from PIL import Image

image_path = "noise_map_001.png"
image = mpimg.imread(image_path)
print(image)

img = Image.open(image_path)

max_colors = 10000

image_colours = img.getcolors(max_colors)


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
