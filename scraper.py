from arcgis_scraper import scrape


stations_url = "https://localview.lancaster.gov.uk/ArcGIS/rest/services/elections/MapServer/2/query?geometry=&geometryType=esriGeometryPoint&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&objectIds=&where=OBJECTID+LIKE+%27%25%27&time=&returnCountOnly=false&orderByFields=OBJECTID&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&outSR=4326&outFields=*&f=pjson"
districts_url = "https://localview.lancaster.gov.uk/ArcGIS/rest/services/elections/MapServer/5/query?text=&geometry=&geometryType=esriGeometryPoint&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&objectIds=&where=OBJECTID+LIKE+%27%25%27&time=&returnCountOnly=false&orderByFields=OBJECTID&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&outSR=4326&outFields=*&f=pjson"
council_id = 'E07000121'


scrape(stations_url, council_id, 'utf-8', 'stations')
scrape(districts_url, council_id, 'utf-8', 'districts')
