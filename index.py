import os 
import time

filter_dict = {
    '.env':'Else',
    '.txt':'Text',
    '.ppt':'PowerPoint',
    '.pptx':'PowerPoint',
    '.pptm':'PowerPoint',
    '.pot':'PowerPoint',
    '.potx':'PowerPoint',
    '.potm':'PowerPoint',
    '.ppa':'PowerPoint',
    '.ppam':'PowerPoint',
    '.htm':'Web',
    '.doc':'Word',
    '.docx':'Word',
    '.docm':'Word',
    '.dot':'Word',
    '.dotx':'Word',
    '.dotm':'Word',
    '.rtf':'Word',
    '.odt':'Word',
    '.csv':'Excel',
    '.xls':'Excel',
    '.xlsx':'Excel',
    '.xlsm':'Excel',
    '.xlsb':'Excel',
    '.xlt':'Excel',
    '.xltx':'Excel',
    '.xltm':'Excel',
    '.xml':'Web',
    '.xlw':'Excel',
    '.tar':'Compress',
    '.zip':'Compress',
    '.7z':'Compress',
    '.php':'Php',
    '.php3':'Php',
    '.php4':'Php',
    '.phtml':'Php',
    '.pyk':'Compress',
    '.class':'Java',
    '.java':'Java',
    '.jar':'Java',
    '.jpeg':'Pictures',
    '.png':'Pictures',
    '.pdf':'Pictures',
    '.jpg':'Pictures',
    '.bmp':'Pictures',
    '.tiff':'Pictures',
    '.tif':'Pictures',
    '.raw':'Pictures',
    '.webp':'Pictures',
    '.heic':'Pictures',
    '.heif':'Pictures',
    '.psd':'Pictures',
    '.git':'Else',
    '.gif':'Pictures',
    '.svg':'Pictures',
    '.html':'Web',
    '.css':'Web',
    '.js':'JS',
    '.mjs':'JS',
    '.c':'C',
    '.h':'C',
    '.cpp':'C++',
    '.cxx':'C++',
    '.hpp':'C++',
    '.rb':'Ruby',
    '.rhtml':'Ruby',
    '.erb':'Ruby',
    '.swift':'Swift',
    '.kt':'Kotlin',
    '.kts':'Kotlin',
    '.py':'Python',
    '.pyc':'Python',
    '.pyd':'Python',
    '.pyo':'Python',
    '.pyw':'Python',
    '.pyz':'Python',
    '.au':'Audio',
    '.mid':'Audio',
    '.midi':'Audio',
    '.mp3':'Audio',
    '.wav':'Audio',
    '.aac':'Audio',
    '.ogg':'Audio',
    '.flac':'Audio',
    '.alac':'Audio',
    '.aiff':'Audio',
    '.aif':'Audio',
    '.wma':'Audio',
    '.mp2':'Audio',
    '.m4a':'Audio',
    '.avi':'Video',
    '.mov':'Video',
    '.mp4':'Video',
    '.qt':'Video',
    '.wmv':'Video',
    '.mkv':'Video',
    '.flv':'Video',
    '.mpeg':'Video',
    '.mpg':'Video',
    '.webm':'Video',
    '.ogv':'Video',
    '.3gp':'Video',
    '.3g2':'Video'
}

# print(set(filter_dict.values()))
# print(len(set(filter_dict.values())))
# print(len(set(filter_dict.keys())))

def start():
    return get_path()

def get_path():
    while(True):
        path = input('Enter path to scan: ')
        try:
            entrys = os.scandir(path)       
        except:
            print('Invalid path!, please try again...')

        return order_fiels(entrys, path)

def order_fiels(entrys, path):
    folders_in_dir = []
    for entry in entrys:
        if entry.is_dir():
            folders_in_dir.append(entry)
        else:
            file_name, file_extention = os.path.splitext(entry)
            if (entry.name).startswith('.'):
                file_extention = entry.name

            if file_extention.lower() in filter_dict.keys():
                new_dir = os.path.join(path, filter_dict[f'{file_extention.lower()}'])

                if os.path.exists(new_dir):
                    os.rename(entry.path, os.path.join(new_dir, entry.name))

                else: 
                    os.mkdir(new_dir)
                    os.rename(entry.path, os.path.join(new_dir, entry.name))

    return will_continue(folders_in_dir, path)


def will_continue(folders_in_dir, path):
    if len(folders_in_dir) < 1:
        print('Nice filtering!,\nprocess DONE!!')
        pass
    else:
        print("\nyou have % s build-in folders in this directory.\n" % len(folders_in_dir))
        continue_check = input('press 1 if you want to keep filtering throw your build-in folders and subfolders!, \npress anythin else to quit the process: ')

        if continue_check == '1':
            keep_filtering(folders_in_dir, path)
        else:
            print('\nNice filtering!,\nprocess DONE!!')
            pass

            
def keep_filtering(folders_in_dir, path):
    delete_folders = input('\nWould you like to delete empty folders?\nPress 1 to delete, press anythin else to NOT delete empty folders: ')

    print('\n continue in 3!')
    time.sleep(1)
    print(' 2')
    time.sleep(1)
    print(' 1!!')
    time.sleep(0.5)
    print('starded...')
    for folder in folders_in_dir:
        folder_path = folder.path
        for roots, dirs, files in os.walk(folder_path):
            for file in files:
                file_name, file_extention = os.path.splitext(file)
                if file_extention.lower() in filter_dict.keys(): 
                    new_dir = os.path.join(path, filter_dict[f'{file_extention.lower()}'])

                    if os.path.exists(new_dir):
                        os.rename(os.path.join(folder_path, file), os.path.join(new_dir, file))
                        # print(os.path.join(folder_path, file), os.path.join(new_dir, file))

                    else: 
                        os.mkdir(new_dir)
                        os.rename(os.path.join(folder_path, file), os.path.join(new_dir, file))
                        # print(os.path.join(folder_path, file), os.path.join(new_dir, file))
            if delete_folders == '1':
                if not any(os.scandir(folder_path)):  
                    os.rmdir(folder_path)
    print('\nFinished Successfully!')

if __name__ == "__main__":
    start()