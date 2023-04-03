from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Range1d, LinearRegression
import pandas as pd

# Load data from Parquet file into pandas DataFrame
df = pd.read_parquet('yellow_tripdata_2023-01.parquet')

# Extract x and y values from data for Vendor ID 2
x = df.loc[df['VendorID'] == 2, 'trip_distance'].head(100)
y = df.loc[df['VendorID'] == 2, 'total_amount'].head(100)

# Define Bokeh ColumnDataSource object
source = ColumnDataSource(data=dict(x=x, y=y))

# Create Bokeh figure
p = figure(title='Yellow Taxi Trip Data', x_axis_label='Trip Distance (miles)', y_axis_label='Total Amount ($)')

# Add scatter plot to figure
p.scatter('x', 'y', source=source, size=5, alpha=0.5)

# Add linear regression line to figure
regression = LinearRegression(source=source, x='x', y='y')
p.add_layout(regression)

# Set axis range to ensure the line is visible
p.x_range = Range1d(0, x.max() + 1)
p.y_range = Range1d(0, y.max() + 1)

# Show figure
show(p)
