import pygame

pygame.init()

font = pygame.font.SysFont('Comic Sans ms', 20)
WHITE = (255 , 255 , 255)

print( """Instructions:-

	When you see R:type any number till 255.
				 G:
				 B:
	If you dont type any number in the range of 255 the application is gonna say something and
	it will crash so you got to rerun the application.
	""" )
color_input1 = int(input("R: "))
color_input2 = int(input("G: "))
color_input3 = int(input("B: "))
color = (color_input1 , color_input2 , color_input3)

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("COLOR GENERATOR")

def draw_text(text , font , text_col , x , y):
    img = font.render(text , True , text_col)
    screen.blit(img, (x, y))

def actual():
	if color_input1 > 255 or color_input2 > 255 or color_input3 > 255:
		print("Kindly write your input less or equal to 255.")
	else:
		WIDTH = 800
		HEIGHT = 800
		screen = pygame.display.set_mode((WIDTH , HEIGHT))
		pygame.display.set_caption("Color generator by Ashutosh Mohanty")
		screen.fill(color)
		draw_text('R: ' + str(color_input1), font, WHITE, 5 , 10)
		draw_text('G: ' + str(color_input2), font, WHITE, 70 , 10)
		draw_text('B: ' + str(color_input3), font, WHITE, 135 , 10)
 
run = True
actual()

while run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()
pygame.quit()
