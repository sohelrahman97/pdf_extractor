import tabula
import numpy as np
import pandas as pd
import os


def schedule_parser(path,filename):
    # Read pdf into list of DataFrame
        # Use this to read from internet source:
            # pdf_path = "https://s3.amazonaws.com/www.srahman.io/media/dummy_timetable.pdf"
            # dfs = tabula.read_pdf(pdf_path, stream=True, pages="1")
        # Use this to convert to CVS file
            # tabula.convert_into(filename, "output.csv", output_format="csv", pages='all')

    dfs = tabula.read_pdf(filename, stream=True, pages="1")

    # Convert into pandas dataframe
    df0 = pd.DataFrame(dfs[0])
    length = len(df0)
    temp_tup = ()
    result = []

    df1 = df0.loc[:,"Day"]
    df2 = df0.loc[:,"Employee"]
    df3 = df0.loc[:,"Sohel"]

    # Collect relevant data into a list of string tuples
    for x in range(length):
        temp_tup = (str(df1[x]), str(df2[x]), str(df3[x]))
        result.append(temp_tup)

    result_formatter(result, filename)


def result_formatter(result, filename):
    length = len(result)
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



