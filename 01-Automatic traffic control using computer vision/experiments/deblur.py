import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import convolve2d as conv2

from skimage import io, color, data, restoration


#astro = color.rgb2gray(data.astronaut())
astro=io.imread('new7iwe.jpg',0)
psf = np.ones((5, 5)) / 25
astro = conv2(astro, psf, 'same')
# Add Noise to Image
astro_noisy = astro.copy()
astro_noisy += (np.random.poisson(lam=25, size=astro.shape) - 10) / 255.
astro += 0.1*astro.std()*(np.random.standard_normal(size=astro.shape))
# Restore Image using Richardson-Lucy algorithm
deconvolved_RL = restoration.wiener(astro, psf, 100)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 5))
plt.gray()

for a in (ax[0], ax[1], ax[2]):
       a.axis('off')

ax[0].imshow(astro)
ax[0].set_title('Original Data')

ax[1].imshow(astro_noisy)
ax[1].set_title('Noisy data')

ax[2].imshow(deconvolved_RL, vmin=astro_noisy.min(), vmax=astro_noisy.max())
ax[2].set_title('Restoration using\nRichardson-Lucy')


fig.subplots_adjust(wspace=0.02, hspace=0.2,
                    top=0.9, bottom=0.05, left=0, right=1)
plt.show()
