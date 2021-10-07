import plotly.express as px
import numpy as np
import pandas as pd
import sys, getopt

def usage( reason = '', exit_code = 0 ):
  if reason != '':
    print( '' )
    print( reason )
    print( '' )

  print(''' usage 
  python plotly-blocker-treemap.py [ -h, --help ] 
  python plotly-blocker-treemap.py [ -i, --info ] [ -s, --show ] 
         [ -t, --tab "name" ] [ --force-csv ] 
         [ -f, --override-fields ] <input_file> 
''')
  sys.exit( exit_code )

# Helpers
def read_file(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

# Filenames 
input_file = ''
output_file = ''
tab_name = ''
fields_file = 'fields.txt'

#Flags 
show_result = False
show_info = False
force_csv = False

try:
  opts, remainder = getopt.getopt(sys.argv[1:],"hist:o:f:",["info","force-csv","tab=","ofile=","override-fields="])
except getopt.GetoptError:
  usage("wrong call", 2)


for opt, arg in opts:
  if opt == '-h':
     usage()
  elif opt in ("-s", "--show"):
     show_result = True
  elif opt in ("-f", "--override-fields"):
     fields_file = arg
  elif opt in ("--force-csv"):
     force_csv = True
  elif opt in ("-i", "--info"):
     show_info = True
  elif opt in ("-o", "--ofile"):
     output_file = arg
  elif opt in ("-t", "--tab"):
     tab_name = arg

if len( remainder ) != 1:
  usage( "Filename missing", 2 )
else:
  input_file = remainder[0]

if not (show_result or (output_file != '')):
  usage("Either '--show' or '-o <filename' have to be specified")

if force_csv or input_file[-4:] == '.csv':
  df = pd.read_csv(input_file, sep=";", dtype = {'Duration': np.float64}, decimal=",")
  print("handling csv - expecting one field to be called 'Duration' and contain blocker duration") 
else:
  if tab_name !='':
    df = pd.read_excel(input_file, sheet_name=tab_name)
  else:
    df = pd.read_excel(input_file)

if show_info:
  print(df)
  print(df.info())

else:
  the_path = read_file(fields_file)

  fig = px.treemap(df, 
                   path=[ px.Constant("Blocker clusters") ] + the_path , 
                   values='Duration',
                   color_discrete_sequence=px.colors.qualitative.Pastel ,
                   color='Category' ,
                  )

  fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
  if show_result:
    fig.show()

  if output_file != '': 
    fig.write_html(output_file)

