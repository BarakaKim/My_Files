#!/usr/bin/env python3
                #BASICS OF SHUTIL AND PSUTIL
import shutil
import psutil
du = shutil.disk_usage ('/') # or shutil.disk_usage ('\\') using windows path
#print (psutil.disk_usage('/')) #disk usage using psutil
print (f'FREE DISK:{(du.free/du.total)*100} %') #the percentage of free disk

print (f'CPU PERCENTAGE: {psutil.cpu_percent(interval=1)}%')
print (f'CPU COUNT:{psutil.cpu_count ()}')
print (F'VIRTUAL MEMORY:\n {psutil.virtual_memory()}')
print (f'dISK PARTIONS:\n {psutil.disk_partitions()}')
print ('\t')

                #HEALTH CHECK IN A COMPUTER
print ('HEALTH CHECK')
#functions for cheking cpu and disk health
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75
    
#If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything ok")