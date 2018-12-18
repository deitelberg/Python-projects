raster = '../Facebook_CIESN_pop_hrsl_ken_v1/hrsl_ken_pop.tif'
counties = '../Data_from_Teddy/unzipped/CountyBoundary2013/CountyBoundary2013.shp'
output = '../Facebook_CIESN_pop_hrsl_ken_v1/Facebook_pop_count.csv'

from rasterstats import zonal_stats
import fiona as fi
import csv


with open(output, 'w') as f:
    writer = csv.writer(f)
    
    i=1
    stats_list = []
    for county in fi.open(counties):
        CID = county['properties']['CID']
        county_name = county['properties']['County']
        
        print('{:<2} {:.<17} {:<1}'.format(i, county_name, CID))
        
        zs = zonal_stats(county, raster, stats="count sum")
        zs[0].update({'CID': CID,'County': county_name})

        print('    {}'.format(zs))

        if i==1:
            header = list(zs[0].keys())
            print(header)
            stats_list.append(header)

        stats_list.append(list(zs[0].values()))
        

        i+=1
        #if i>3:
        #    break
    writer.writerows(stats_list)

#print('\n\n{}'.format(stats_list))