from PIL import Image


img = Image.open('../imgs/leg.jpg')
# img.show()

#
# print(f"image size = {img.size}")
# print(f"image format = {img.format}")
# print(f"image mode = {img.mode}")


# img.show()

# dimentions of the crop
box = (100, 100, 300, 300)


newImg = img.crop(box)
# newImg.show()

# save the new cropped image
# newImg.save('../imgs/legNew.jpg')

# copiedImg = newImg.copy()
# copiedImg.show()
# print(copiedImg.size, copiedImg.mode, copiedImg.format)

# rotatedImg = img.rotate(23)
# rotatedImg.show()
#
# for i in range(361):
#     image = img.rotate(i)
#     image.save(f'{i}_test.jpg')




