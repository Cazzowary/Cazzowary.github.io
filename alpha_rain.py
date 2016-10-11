#alpha rainfall
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "alphayear.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rain = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rain = int(row[21])
            
