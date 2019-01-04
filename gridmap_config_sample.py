# This is a sample config file for tiled_gridmap_tesselation.ipynb

kenya_counties = '<path to counties shapefile>'
kenya_counties_msOriginal = '<path to map shaper counties shapefile>'
kenya_counties_msSimplified = '<path to map shaper simplified counties shapefile>'

epsg = 32662 #Kenya
#epsg = 5070 #USA

seed_location = 'lowerleft'
round_to = 10
num_shape_divisor = 6

symbology_column = 'County' #Kenya

vertices_col = 'vertices'
geom_col = 'geometry'

tile_id = 'tile_id'
admin_id = 'CID'