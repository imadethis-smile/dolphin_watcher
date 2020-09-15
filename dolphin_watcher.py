import subprocess
import time
import os

file_path_hours = os.getcwd() + '/dolphin_hours.txt'

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())


intial_time = time.time()
while(True):
    if(process_exists('dolphin.exe')):
        print('dolphin running, counting hours')
        session_start_time = time.time()
        while(process_exists('dolphin.exe')):
            start_time = time.time()
            time.sleep(60)
            try:
                with open(file_path_hours, 'r') as f:
                    initial_hours = float(f.readline())
            except:
                initial_hours = 0.0
            added_time = (time.time() - start_time) / 3600.0
            new_hours = initial_hours + added_time
            print('new hours: ', str(new_hours))
            with open(file_path_hours, 'w') as f:
                f.writelines(str(new_hours))
        print('dolphin closed, sleeping')
        print('session lasted: '+str((time.time()-session_start_time)/3600.0)+' hours')
    else:
        time.sleep(60)
