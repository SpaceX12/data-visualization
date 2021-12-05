import pandas as pa
import plotly.express as px
import csv

df = pa.read_csv('data.csv')

fig = px.scatter(df, 
                x = df.groupby('student_id')['attempt'],
                y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'],
                size= 'attempt', 
                color= 'attempt',
                size_max = 4)
fig.show()