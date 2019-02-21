from dc_base_scrapers.arcgis_scraper import UnsortedArcGisScraper


stations_url = "https://localview.lancaster.gov.uk/ArcGIS/rest/services/elections/MapServer/2/query?geometry=&geometryType=esriGeometryPoint&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&objectIds=&where=OBJECTID+LIKE+%27%25%27&time=&returnCountOnly=false&orderByFields=OBJECTID&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&outSR=27700&outFields=*&f=pjson"
districts_url = "https://localview.lancaster.gov.uk/ArcGIS/rest/services/elections/MapServer/5/query?text=&geometry=&geometryType=esriGeometryPoint&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&objectIds=&where=OBJECTID+LIKE+%27%25%27&time=&returnCountOnly=false&orderByFields=OBJECTID&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&outSR=27700&outFields=*&f=pjson"
council_id = 'E07000121'


stations_scraper = UnsortedArcGisScraper(stations_url, council_id, 'utf-8', 'stations')
stations_scraper.scrape()
districts_scraper = UnsortedArcGisScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
