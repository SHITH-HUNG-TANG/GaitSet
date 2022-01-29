import os 

input_path = 'G:/TANG/repository/dataSet/GaitDatasetB-silh/GaitDatasetB-silh/GaitDatasetB-silh'
output_path = './data/CASIAB/'

os.system("python pretreatment.py --input_path=%s --output_path=%s" % (input_path, output_path))