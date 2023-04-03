from bokeh.plotting import figure, show
import pandas as pd
from bokeh.models import ColumnDataSource, Slope, Range1d
import numpy as np

#read data from parquet file and convert to pandas dataframe
df = pd.read_parquet('yellow_tripdata_2023-01.parquet')

#only get a subset of columns
df = df[['trip_distance','total_amount','VendorID']]


#get only for vendor id 2,1000 rows
x = df[df['VendorID'] == 2]['trip_distance'].head(1000)
y = df[df['VendorID'] == 2]['total_amount'].head(1000)


# create a new plot with a title and axis labels
p = figure(title="Yellow Taxi trip Data", x_axis_label='Trip Distance in miles', y_axis_label='Total  Amount')

# add a line renderer with legend and line thickness to the plot
# p.vbar(x=x,top= y, legend_label="Distance.",width=0.5, bottom=0, color="red")
#line plot
p.line(x, y, legend_label="Distance.", line_width=2)

show(p)