print('Welcome to my search by Anyaele Destiny Chinaemere')
search = input('Enter the file name you want to search : ').lower()
storage = input('choose storage point (phone or sdcard): ')
files = []
import os
def get_all_files(path) :
    for searching in os.listdir(path) :
        temp = path
        if os.path.isdir(temp + f'/{searching}') == True :
            temp += f'/{searching}'
            get_all_files(temp)
        elif os.path.isfile(temp + f'/{searching}') == True :
            if searching.lower() == search or searching.lower().startswith(search) == True :
                files.append(temp + f'/{searching}')
        if  searching == os.listdir(path)[-1] :
            path = temp.replace(f'/{searching}','',1)
search_path = os.getcwd()
if storage.lower() == 'phone' :
    get_all_files(search_path)
elif storage.lower() == 'sdcard' :
    os.chdir('/storage')
    pos = os.listdir()
    for i in pos :
        if i == 'emulated' or i == 'self' :
            continue
        os.chdir(f'/storage/{i}')
        search_path = os.getcwd()
        get_all_files(search_path)
else :
    get_all_files(search_path)
    os.chdir('/storage')
    pos = os.listdir()
    for i in pos :
        if i == 'emulated' or i == 'self' :
            continue
        os.chdir(f'/storage/{i}')
        search_path = os.getcwd()
        get_all_files(search_path)
if len(files) == 0 :
    print(f'No files called {search}')
    print('Are you sure thats the file name')
else :
    print('These are the paths to your search')
    for result,searched in enumerate(files) :
        result += 1
        print(result,' : ',searched)
print('Thanks for using our searcher')
