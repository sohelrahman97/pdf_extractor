import tabula
import pandas as pd
import numpy as np
import os


def schedule_parser(path,filename):
    # Read pdf into list of DataFrame
    dfs = tabula.read_pdf(filename, pages='all')

    tabula.convert_into(filename, "output.csv", output_format="csv", pages='all')

    df = pd.read_csv('output.csv', sep=',', header=1, dtype=str, nrows=29)

    df1 = df.loc[:]['Day']
    df2 = df.loc[:]['Employee']
    df3 = df.loc[:]['Sohel']

    result = []
    temp_tup = ()

    length = len(df3)

    for x in range(length):
        temp_tup = (str(df1[x]), str(df2[x]), str(df3[x]))
        result.append(temp_tup)

    #temp = result[0]
    #print(temp[2])
    result_formatter(result, filename)

    os.remove('output.csv')


def result_formatter(result, filename):
    length = len(result)
    i=0
    sanitized_string = ''

    for x in range(length):
        temp = result[x]

        #print(temp)
        if(temp[1]=='In' and temp[2]!='nan'):
            sanitized_string += temp[0] + ', ' + temp[2] + ' - '

        if(temp[1]=='Out' and temp[2]!='nan'):
            sanitized_string += temp[2] + '\n'

    sanitized_string = "Hey mom,\n\nHere's the new work schedule:\n\n" + sanitized_string + '\nSohel'

    curr_filename = "result - " + filename[:-4] + '.txt'

    #print(sanitized_string)
    f = open(curr_filename, "w")
    f.write(sanitized_string)
    f.close()

#scan directory \docs\ to see how many schedule PDF files are there, add them all to a list
path = os.path.dirname(os.path.realpath(__file__))
obj = os.scandir(path)
files = []

print("Files and Directories in '% s':" % path)
for entry in obj :
    if entry.is_file():
        print(entry.name)
        file_extension = entry.name[-3:]
        if(file_extension == 'pdf'):
            files.append(entry.name)
            print(" - (ADDED FOR PROCESSING)")
        

obj.close()

length = len(files)

#parse each file 
for x in range(length):
    schedule_parser(path,files[x])



