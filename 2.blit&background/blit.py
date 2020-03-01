# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the program logo
    logo = pygame.image.load("eg.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("useless window")
     
    #Make the image transparent
    logo.set_alpha(128) # 0=> fully transparent 255=>fully opaque

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((512,512))


    #fill the background
    screen.fill((100,25,65))
    pygame.display.flip()


    #Copy the image onto the window using blit()
    screen.blit(logo,(10,10))
    pygame.display.flip()

    # define a variable to control the main loop (Removing this loop will make the window appear and dissappear)
    run = True
    
    # main loop
    while run:
        # event handling, gets all event from the event queue
        

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                run = False
     
    
if __name__=="__main__":
    # call the main function
    main()