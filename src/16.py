import os
import requests

def download_files(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
    
    response = requests.get('https://example.com/file.txt')
    with open(os.path.join(directory, 'downloaded_file.txt'), 'wb') as f:
        f.write(response.content)

directory_path = '/path/to/your/project'
download_files(directory_path)
