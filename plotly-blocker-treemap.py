import plotly.express as px
import numpy as np
import pandas as pd
import sys

#df = pd.read_csv('./data/BlockersPrepared.csv', sep=";", dtype = {'Duration': np.float64}, decimal=",")
df = pd.read_excel('./data/IgusBlockersForHeatmap.xlsx', sheet_name='IgusBlockerFuerHeatmap2')
df = pd.read_excel('./data/IgusBlockersForHeatmap.xlsx', sheet_name='IgusBlockerFuerHeatmap')

if len(sys.argv) > 1 and (sys.argv[1] == "info"):
  print(df)
  print(df.info())

else:

  fig = px.treemap(df, 
                   path=[
                          px.Constant("Blocker"), 
                          'WorkOrIdleTime', 
                          'should_have_been_andon_cord',
                          'Category', 
                          'Explanation'], 
                   values='Duration',
                   color_discrete_sequence=px.colors.qualitative.Pastel ,
                   color='Category' ,
                  )

  fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
  fig.show()
