import csv  # https://docs.python.org/3/library/csv.html
from unesco.models import Site, Category, States, Region, Iso


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    # Format
    # name_0,description_1,justification_2,
    # year_3,longitude_4,latitude_5,
    # area_hectares_6,category_7,states_8,region_9,iso_10
    for row in reader:
        # print(row)
        try:
            y = int(row[3])
            lg = float(row[4])
            lt = float(row[5])
            ah = float(row[6])
        except:
            y = None
            lg = None
            lt = None
            ah = None
        c, created = Category.objects.get_or_create(name=row[7])
        s, created = States.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])
        s = Site(name=row[0], description=row[1], justification=row[2],
                year=y, longitude=lg, latitude=lt, 
                area_hectares=ah, category=c, states=s, region=r, iso=i)
        s.save()
