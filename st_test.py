#strptime test

from datetime import datetime
first_date = datetime.strptime('Thursday-October-6-2016', '%A-%B-%d-%Y')

print(first_date)
