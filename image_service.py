import requests
import csv
from PIL import Image
from io import BytesIO
import os

folder_path = 'C:\\Users\\sesa7\\Downloads\\tablecloth'
infographic1 = Image.open("C:\\Users\\sesa7\\Downloads\\infographics1.png")
infographic2 = Image.open("C:\\Users\\sesa7\\Downloads\\infographics2.png")


with open('hype.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        folder_name = row['id']
        if not os.path.exists(folder_name):
            new_path = os.path.join(folder_path, folder_name)
            print(new_path, end=' ')
            os.makedirs(new_path)

        response1 = requests.get(row['photo1_url'])
        response2 = requests.get(row['photo2_url'])

        if response1.status_code == 200:    
            photo1 = Image.open(BytesIO(response1.content))
            print("image1", end=' ')
            photo1.paste(infographic1, (0, 0), infographic1)
            save_path1 = os.path.join(new_path, '1.png')
            photo1.save(save_path1)
        else: print("not found image1", end=' ')
        
        if response2.status_code == 200:
            photo2 = Image.open(BytesIO(response2.content))
            print("image2", end=' ')
            photo2.paste(infographic2, (0, 0), infographic2)
            save_path2 = os.path.join(new_path, '2.png')
            photo2.save(save_path2)
        else:
            if response1.status_code == 200:
                photo2 = Image.open(BytesIO(response1.content))
                print("image2", end='\n')
                photo2.paste(infographic2, (0, 0), infographic2)
                save_path2 = os.path.join(new_path, '2.png')
                photo2.save(save_path2)
        
        # if not os.listdir(new_path):
        #     os.rmdir(new_path)
    
print("success")