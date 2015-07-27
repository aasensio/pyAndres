import numpy as np
import matplotlib.pyplot as pl
import matplotlib.animation as animation

def blink(ima1, ima2, interval=250, fig=None):
	which = 0
	if (fig == None):
		fig = pl.figure()
	im = pl.imshow(ima1)

	def updatefig(*args):
		global which
		if (which == 0):
			im.set_array(args[0])
			which = 1
		else:
			im.set_array(args[1])
			which = 0
		return im,

	ani = animation.FuncAnimation(fig, updatefig, interval=interval, blit=True, fargs=(ima1,ima2))

im1 = np.random.randn(100,100)
im2 = np.random.randn(100,100)

blink(im1, im2)