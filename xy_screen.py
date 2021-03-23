import numpy as np

def calculate_x_y(hypotenuse, aspectratio_choice, resolution):
	aspectratio = (16.0/9) if aspectratio_choice is 1 else (21.0/9)
	# (aspectratio^2 + 1)height^2 = hypotenuse^2
	height = np.sqrt(hypotenuse**2 / (aspectratio**2 + 1))

	return aspectratio*height, height, resolution/height

hypotenuse = input('enter the diagonal length of your screen in inches\n')
aspectratio_choice = input('aspect ratio - enter 1 for 16:9, or 2 for 21:9\n')
resolution = input('what is the resolution of the monitor in pixels? ex. enter 1080, 1440, or 2160\n')

width, height, ppi = calculate_x_y(float(hypotenuse), int(aspectratio_choice), int(resolution))


print(f'\n(WxH) {width:.1f}"x{height:.1f}"')
print(f'Area: {height*width:.1f}"2')
print(f'PPI: {ppi:.1f}')
