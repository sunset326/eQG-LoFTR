from PIL import Image

img0 = Image.open('temp8.23/3.30.jpg')
#img1 = Image.open('branch/5.11.jpeg')

img0.rotate(30,expand=False).save('temp8.23/3.30_rt30.jpg')#旋转45度
#img1.rotate(30,expand=True).save('branch26/5.11_rt30.jpeg')#旋转45度

img0.rotate(20,expand=False).save('temp8.23/3.30_rt20.jpg')#旋转45度
#img1.rotate(20,expand=True).save('branch/5.11_rt20.jpeg')#旋转45度

img0.rotate(45,expand=False).save('temp8.23/3.30_rt45.jpg')#旋转45度
