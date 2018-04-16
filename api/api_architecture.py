""" Resources exposed to client requests """


# All resources are get resources, I simply will allow clients to access (GET) the data about particular resources
"""
http://utahskiareas.com/api/v1.0/basetotals
http://utahskiareas.com/api/v1.0/twentyfourhourtotals
http://utahskiareas.com/api/v1.0/basetotals/[area_id]
http://utahskiareas.com/api/v1.0/twentyfourhourtotals/[area_id]
http://utahskiareas.com/api/v1.0/areas
http://utahskiareas.com/api/v1.0/areas/[area_id]

 base/twenty four hour totals will have the following fields:
area_id: Primary Key to identify each area. Numeric type
area_name: Name of each area. String
base/twenty_four_hour_total: Total snowfall for base/past twenty four hours. Integer
crawled_at: Date the snowfall total was last updated at. Date

"""




## Perhaps add in the NOAA snowfall total, to cross reference with the ski areas api, eventually will need to get all the same twenthy four hour totals

