'''
    A module helps changing file created, modified and last access timestamp
    
    Use the following site to get Epoch time if you want to set file to a specific time
    https://www.epochconverter.com/
    
    Install win32-sectctime if needed
    pip install win32-setctime
    
    NOTE: this code only works on Windows OS
'''
import os
import sys
import time
from win32_setctime import setctime

class ChangeFileTime:
    '''
		Each file contains three timestamps: created, modified and last access
		use setctime(self.fn, self.curr_timestamp) to update created time
		use os.utime(filename, (last_access, modified)) update last access, modified
	'''
    def __init__(self, file_name):
        self.file_name = file_name
        self.curr_timestamp = time.time()

    def set_file_with_current_time(self):
        '''Set the file with the current timestamp'''
        setctime(self.file_name, self.curr_timestamp)
        os.utime(self.file_name, (self.curr_timestamp, self.curr_timestamp))

    def set_file_time_with_delta_access(self, delta): ### default to add one hour
        '''Set the file with the current timestamp and add more the last access'''
        setctime(self.file_name, self.curr_timestamp)
        os.utime(self.file_name, (self.curr_timestamp + delta, self.curr_timestamp))

    def set_file_time_based_on_created(self):
        '''Set all three timestamp same as created time'''
        timestamp = os.path.getctime(self.file_name)
        os.utime(self.file_name, (timestamp, timestamp))

    def set_file_time_user_provided(self, created, modified, last_access):
        '''Set all three timestamp same as the current created time'''
        setctime(self.file_name, created)
        os.utime(self.file_name, (last_access, modified))

def main(argv):
    '''main method, mainly for testing'''
    if len(argv) == 0:
        print("ERROR: missing input file name\n")
        sys.exit(1)

    change_file_time_obj = ChangeFileTime(argv[1])
    if len(argv) == 2: ### file name only
        change_file_time_obj.set_file_with_current_time()
    if len(argv) == 3: ### file name and delta
        change_file_time_obj.set_file_time_with_delta_access(int(argv[2]))

if __name__ == "__main__":
    main(sys.argv)
