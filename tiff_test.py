
# define the TIFF file path
tiff_file = 'C:\\Users\\xxx\\Desktop\\tiff test\\tiff_image.tiff'

# Open the TIFF file
with Image.open(tiff_file) as img:
    # Save the TIFF file as a PDF
    img.save(tiff_file.replace('.tif', '.pdf'), 'PDF')

print("The TIFF file has been converted to a PDF.")
