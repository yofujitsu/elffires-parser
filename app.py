from PIL import Image

# Открываем изображение с инфографикой
infographic = Image.open("C://Users/sesa7/Downloads/infographic.png")

# Перебираем 100 изображений для обработки
    # Открываем изображение для наложения инфографики
image_path = "C://Users/sesa7/Downloads/1152448130.jpg"
image = Image.open(image_path)
    
    # Налагаем инфографику на изображение
image.paste(infographic, (0, 0), infographic)
    
    # Сохраняем результат
image.save(f'result.png')

print('success!')