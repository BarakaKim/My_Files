#!/bin/bash
import shutil
import psutil
                    #SHUTIL
du = shutil.disk_usage ('/') # or shutil.disk_usage ('\\') using windows path
#print (psutil.disk_usage('/')) #disk usage using psutil
print (f'FREE DISK:{(du.free/du.total)*100} %') #the percentage of free disk
                     #PSUTIL
print (f'CPU PERCENTAGE: {psutil.cpu_percent(interval=1)}%')
print (f'CPU COUNT:{psutil.cpu_count ()}')
print ('\t')
print (F'VIRTUAL MEMORY:\n {psutil.virtual_memory()}')
print ('\t')
print (f'dISK PARTIONS:\n {psutil.disk_partitions()}')
print (f'your free disk space is: {(shutil.disk_usage('/').free)/shutil.disk_usage('/').total *100)}')
