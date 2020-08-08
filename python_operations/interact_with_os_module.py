import os

# Get the absolute path of all the Files in current directory



def list_of_file_in_path(dir):
    list_of_files = os.listdir(dir)
    return list_of_files

def abs_path_of_files_in_dir(dir):
    list_of_files = list_of_file_in_path(dir)
    abs_path = []
    for file in list_of_files:
        abs_path.append(os.path.join(dir, file))
    return abs_path

def  free_space_in_current_dir(dir):
    # Only works in Linux Environment
    statvfs = os.statvfs(dir)
    fragment = statvfs.f_frsize
    avail_block_count = statvfs.f_bavail
    free_space = fragment * avail_block_count
    return free_space


if __name__ == "__main__":
    current_dir = os.getcwd()
    print (list_of_file_in_path(current_dir))
    print (*abs_path_of_files_in_dir(current_dir), sep="\n")
    os.mkdir('newDir')
    os.rename('newDir', 'newDir2')
    os.rmdir('newDir2')
    print (os.path.exists(current_dir))
    user_id = os.getlogin()
    print (user_id)
    print (free_space_in_current_dir(current_dir)) # Only works in Linux Environment
    # os.path.isfile(file_name) # check if file is present
    # os.path.getsize(file_name) # check file size