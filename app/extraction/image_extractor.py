import fitz
import os

def extract_images(file, output_folder="data/images"):
    file.seek(0)
    doc = fitz.open(stream=file.read(), filetype="pdf")

    os.makedirs(output_folder, exist_ok=True)
    image_paths = []

    for page_index in range(len(doc)):
        page = doc[page_index]
        images = page.get_images(full=True)

        for i, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            path = f"{output_folder}/page{page_index}_img{i}.png"

            with open(path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(path)

    return image_paths