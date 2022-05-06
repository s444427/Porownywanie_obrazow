from PIL import Image
import numpy as np

if __name__ == '__main__':
    # Check inputs
    im = Image.open('raw_sea.jpg').convert('L')
    pix = im.load()

    print(pix[0, 0])
    print(im.size)  # Get the width and height of the image for iterating over

    a, b = 0, 0
    step_size = [8, 8]
    frame_size = [im.size[0] - step_size[0], im.size[1] - step_size[1]]

    # Single frame - frame comparison
    step_mse = np.zeros((8, 8))

    # Frame to all other frames
    frame_mse = np.zeros((frame_size[0], frame_size[1]))

    # All frames to all frames
    # pic_mse = np.zeros(( int(im.size[0]/8), int(im.size[1]/8) ))


    # Frame mse
    for c in range(frame_size[0]):
        for d in range(frame_size[1]):
            # Step mse
            color_diff = 0
            for i in range(step_size[0]):
                for j in range(step_size[1]):
                    color_diff += (pix[a + i, b + j] - pix[c + i, d + j]) ** 2

            # TODO if ramki się nachodzą
            if True:
                print("x")
            else:
                frame_mse[c, d] = round(color_diff)

    print(frame_mse.shape)
