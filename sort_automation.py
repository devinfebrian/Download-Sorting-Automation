import os, shutil
from pathlib import Path

# GLOBAL VARIABLES
# PATH_DOWNLOADS = r'C:\Users\USER\Downloads' # LOCAL
PATH_DOWNLOADS = Path.home() / 'Downloads' # Universal


# DEFINE SORTING RULES
CATEGORIES = {
  '_Images'    : ['.jpg', '.jpeg', '.png'],
  '_GIF'       : ['.gif'],
  '_Videos'    : ['.mp4', '.mkv', '.avi', '.mov'],
  '_Audios'    : ['.mp3', '.m4a'],
  '_Docs'      : ['.pdf', '.docx', '.txt', '.pptx'],
  '_ZIPs'      : ['.zip', '.rar', '.7z'],
  '_Installer' : ['.exe', '.msi'],
  '_Code'      : ['.py', '.js', '.html', '.css', '.md', '.jsx', '.ipynb'],
  '_Data'      : ['.csv', '.xlsx', '.sql'],
  '_Design'    : ['.fig', '.psd', '.svg']

}


def get_file_cat(filename):
  """ Find Sorting Folder by Name.
  :param filename: Filename inside of Downloads Folder
  :return:         Name of Sorting Folder"""

  # Ignore Sorting Folder
  if filename.startswith('_'):
    return None

  # FOLDER
  filepath = os.path.join(PATH_DOWNLOADS, filename)
  if os.path.isdir(filepath):
    return '_Folders'

  # FILE
  else:
    # OPTION A FOR FILE EXTENSION
    # for cat, list_keyword in CATEGORIES.items():
    #   if file_extension.lower() in list_keyword:
    #     return cat
    
    file_extension = '.' + filename.split('.')[-1]
    for cat,list_keyword in CATEGORIES.items():
      for keyword in list_keyword:
        if keyword.lower() in filename.lower():
          return cat

    print(f"{file_extension} - Not Supported. File: ({filename}) Placed in Others")
    return '_Others' # NOT IN THE RULES FOR CATEGORIZING LATER ON
    print(filename) 
  


# READ ALL FILES
def sort_downloads():

  # PlaceHolders
  count, fails = 0, 0
  failed_msgs = []
  
  all_files = os.listdir(PATH_DOWNLOADS)
  folders = [f for f in all_files if os.path.isdir(os.path.join(PATH_DOWNLOADS, f)) and not f.startswith('_')]
  files = [f for f in all_files if not os.path.isdir(os.path.join(PATH_DOWNLOADS, f))]

  # REPORT TO CONSOLE
  print('-'*40)
  print("Scanning Downloads Folder...")
  print(f"Folders Found: {len(folders)} (Will be ignored)")

  if files:
    print(f"Files Found: {len(files)}")
    print('\n-------------Sorting-------------')
  else:
    print("Files Found: 0")
    print('\n Nothing to sort here...')


  for file in all_files:
    dir_name  = get_file_cat(file)

    if dir_name:
      # Create Sorting Folders
      dir_filepath = os.path.join(PATH_DOWNLOADS, dir_name)
      if not os.path.exists(dir_filepath):
        os.makedirs(dir_filepath)

      # DEFINE OLD/NEW PATH
      old_path = os.path.join(PATH_DOWNLOADS, file)
      new_path = os.path.join(PATH_DOWNLOADS, dir_name, file)

      # MOVE FILE
      try:
        shutil.move(old_path, new_path)
        print(f"{dir_name}/{file}")
        count += 1
      except Exception as e:
        failed_msgs.append(f"{dir_name}/{file} - {e}")
        fails += 1

  if count:
    print(f"\n Succesfully Sorted {count} files.")

  if fails:
    print('-'*40)
    print(f"Failed to Sort {fails} Files.")
    for msg in failed_msgs:
      print(msg)

# MAIN
if __name__ == '__main__':
  sort_downloads()