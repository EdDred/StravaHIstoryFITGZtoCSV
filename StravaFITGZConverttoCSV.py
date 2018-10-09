import gzip
import shutil
import os
import pathlib
from fitparse import FitFile
import csv

'''

Converting Stravas .gz route file to a csv file
1. Extact all .gz files in directory to fit fitfiles using extract()
2. Convert all fit files in directory to CSV using convertfittocsv()

'''

# define the path
currentDirectory = pathlib.Path('.')

# define the pattern
currentPattern = "*.gz"

#def extract(sourcefile,fit):
def extract():
    '''
    Extract files in the python files directory ending with .gz to .fit
    Backlog: add other file_extension

    '''
#One file test version
    # for currentFile in currentDirectory.glob(currentPattern):
    #     print(currentFile)
    #     with gzip.open(sourcefile, 'rb') as f_in:
    #         with open(fit, 'wb') as f_out:
    #             shutil.copyfileobj(f_in, f_out)
    # return

#Loop version for all files
    currentPattern = "*.fit.gz"
    for currentFile in currentDirectory.glob(currentPattern):
        with gzip.open(currentFile, 'rb') as f_in:
            filename_w_ext =os.path.basename(currentFile)
            filename, file_extension = os.path.splitext(filename_w_ext)
            with open(filename, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    return


# Get all data messages that are of type record
# def convertfittocsv(csv_file,csv_columns,fitfile):
# #Convert the fitfile to a csv file
#     '''
#     convertfittocsv(csv_file,csv_columns,fitfile):
#     Convert the fitfile to a csv file
#     csv_file: target .csv FitFile
#     Csv_columns : headers of FitFile
#     fitfile: the input .fit file
#
#     '''
# #Working conversion to CSV for 1 file
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(
#         csvfile, fieldnames = ['altitude','enhanced_altitude', 'position_lat','position_long','heart_rate','timestamp','calories', 'temperature', 'left_right_balance', 'right_torque_effectiveness', 'enhanced_speed', 'left_pedal_smoothness', 'right_pedal_smoothness', 'power', 'grade', 'distance', 'accumulated_power', 'cadence', 'left_torque_effectiveness', 'speed']
#         )
#         #Assemble and write the header
#         writer.writeheader()
#         for record in fitfile.get_messages('record'):
#             print(record)
#             waarde = record.get_values()
#             #Write every dictionary line as a line corresponding to correct key
#             writer.writerow(waarde)
#             print(waarde)
#     return

# Setup for multiple file conversion from fit to CSV
def convertfittocsv(csv_columns,fitPattern):
    for currentFile in currentDirectory.glob(fitPattern):

        filename_w_ext =os.path.basename(currentFile)
        filename, file_extension = os.path.splitext(filename_w_ext)
        fitfile = FitFile(filename_w_ext)
        with open(filename+".csv", 'w') as csvfile:
            writer = csv.DictWriter(
            csvfile, fieldnames = ['altitude','enhanced_altitude', 'position_lat','position_long','heart_rate','timestamp','speed', 'right_torque_effectiveness', 'power', 'cadence', 'enhanced_speed', 'distance', 'grade', 'left_torque_effectiveness', 'accumulated_power', 'calories', 'left_pedal_smoothness', 'right_pedal_smoothness', 'left_right_balance', 'temperature']
            )
            #Assemble and write the header
            writer.writeheader()
            #writer.writerow(filename)
            for record in fitfile.get_messages('record'):
                waarde = record.get_values()
                #Write every dictionary line as a line corresponding to correct key
                writer.writerow(waarde)
                print(waarde)

    return

#One File execution
#sourcefile = "1853020809.fit.gz"
#fit= "1853020809.fit"
csv_columns={'altitude','enhanced_altitude', 'position_lat','position_long','heart_rate','timestamp'}
#extract(sourcefile,fit)
# extract()
# fitfile = FitFile('1853020809.fit')
# csvfile = '1853020809_test.csv'
# convertfittocsv(csvfile,csv_columns,fitfile)

#Setup for multiple files extract and convert
# Patterns =["*.tcx.gz","*.fit.gz"]
# for pat in Patterns:
#     extract(pat)
extract()
ConvertPattern = "*.fit"
convertfittocsv(csv_columns,ConvertPattern)
