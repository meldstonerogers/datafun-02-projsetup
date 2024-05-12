"""Module 2 Creating Project Folders"""

#import dependencies 
import pathlib
import time
import MelissaStoneRogers_utils

#create folder for range
def create_year_folders(start_year, end_year):
    """
    Creates folders for a given range of years.
    :param start_year: First year, e.g. 2010
    :param end_year: Final year, e.g. 2024
    """
    for year in range(start_year, end_year + 1):
        folder_name = str(year)
        pathlib.Path(folder_name).mkdir(exist_ok=True)

#create folder from list
def create_folders_from_list(folder_list):
    for folder in folder_list:
        pathlib.Path(folder).mkdir(exist_ok=True)

#create prefixed folders
def create_prefixed_folders(folder_list, prefix):
    for folder in folder_list:
        pathlib.Path(f"{prefix}-{folder}").mkdir(exist_ok=True)

#create folders periodically 
def create_folders_periodically(duration, period):
    start_time = time.time()
    while time.time() - start_time < duration: 
        current_time = time.time() - start_time
        pathlib.Path(f"Folder created at {round(current_time)} seconds").mkdir(exist_ok=True)
        time.sleep(period)

#define main function 
def main():
    ''' Main function to demonstrate module capabilities. '''
    #print byline from imported module
    print(f"Byline: {MelissaStoneRogers_utils}")

    # Call function 1 to create folders for a range (e.g. years)
    create_year_folders(start_year=2010, end_year=2024)

    # Call function 2 to create folders given a list
    folder_names = ['month-week1', 'month-week2', 'month-week3']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['week1', 'week2', 'week3']
    prefix = 'month'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  
    create_folders_periodically(duration_secs, 1)

   
if __name__ == '__main__':
    main()
