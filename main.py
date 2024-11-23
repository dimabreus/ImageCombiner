import os
from tkinter import Tk, filedialog

from PIL import Image


def select_file(title):
    Tk().withdraw()
    file_path = filedialog.askopenfilename(title=title,
                                           filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if not file_path:
        raise ValueError("Файл не был выбран!")
    return file_path


def combine_images_with_alpha(image1_path, image2_path, output_path):
    image1 = Image.open(image1_path).convert("RGBA")
    image2 = Image.open(image2_path).convert("L")

    if image1.size != image2.size:
        raise ValueError("Размеры изображений должны совпадать!")

    r, g, b, _ = image1.split()
    combined_image = Image.merge("RGBA", (r, g, b, image2))

    combined_image.save(output_path, "PNG")
    print(f"Результат сохранён в {output_path}")


def main():
    print("Выберите первое изображение (основное, с цветами)...")
    image1_path = select_file("Выберите первое изображение (JPG/PNG)")

    print("Выберите второе изображение (чёрно-белое, для альфа-канала)...")
    image2_path = select_file("Выберите второе изображение (JPG/PNG)")

    output_dir = os.path.dirname(image1_path)
    output_path = os.path.join(output_dir, "result.png")

    try:
        combine_images_with_alpha(image1_path, image2_path, output_path)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
