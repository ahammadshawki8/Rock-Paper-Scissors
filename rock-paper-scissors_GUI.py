import pygame
import random
import time
pygame.init()

win = pygame.display.set_mode((650,600))
pygame.display.set_caption("Rock-Paper-Scissors")
clock = pygame.time.Clock()
player_area = (0,0)
comp_area = (395,0)


bg = pygame.image.load("resources/main.jpg")
poster = pygame.image.load("resources/poster.jpg")
rock = pygame.image.load("resources/rock.png")
paper = pygame.image.load("resources/paper.png")
scissors = pygame.image.load("resources/scissors.png")
won = pygame.image.load("resources/won.jpg")
lost = pygame.image.load("resources/lost.jpg")
point = pygame.image.load("resources/point.jpg")
choose = pygame.image.load("resources/choose.jpg")
thanks = pygame.image.load("resources/thanks.jpg")
proposal = pygame.image.load("resources/proposal.jpg")
code_loop = pygame.image.load("resources/code_loop.jpg")
the_as8_org = pygame.image.load("resources/the_as8_org.jpg")

click = pygame.mixer.Sound("resources/click.wav")
rock_s = pygame.mixer.Sound("resources/rock.wav")
paper_s = pygame.mixer.Sound("resources/paper.wav")
scissors_s = pygame.mixer.Sound("resources/scissors.wav")
music = pygame.mixer.music.load("resources/music.mp3")
pygame.mixer.music.play(-1)

def screen_timer(win,time,slide):
    i = 0
    while i < time+1:
        clock.tick(60)
        win.blit(slide, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        i += 1
        pygame.display.update()

def write(win,string,size,pos):
    font = pygame.font.SysFont("comicsans",size)
    text = font.render(string, 1, (0,0,0))
    win.blit(text, pos)
    pygame.display.update()


def kamla(win,bg,player_score,comp_score,player_choice,comp_choice,player_area,comp_area,target):
    win.blit(bg, (0,0))
    win.blit(player_choice, player_area)
    win.blit(comp_choice, comp_area)
    write(win,"P",80,(20,20))
    write(win,"C",80,(600,20))
    write(win, "Target "+str(target),40,(270,30))
    write(win,"Player " + str(player_score) + " : " + str(comp_score) + " Computer", 20, (259,300))
    pygame.display.update()

def hamla(condition,win,bg,player_score,comp_score,player_choice,comp_choice,player_area,comp_area,target):
    player_score += 1
    kamla(win,bg,player_score,comp_score,player_choice,comp_choice,player_area,comp_area,target)
    time.sleep(.2)




counter = -1
extra_counter = 0
player_score = 0
comp_score = 0
target = 0
player_choice = None
comp_choice = None

while True:
    clock.tick(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    
    if counter == -1:
        screen_timer(win,200,poster)
        counter = 0

    if counter == 0:
        win.blit(point, (0,0))
        pygame.display.update()
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            click.play()
            if (x>175 and x<475) and (y>150 and y<200):
                target = 3
                counter = 1
                time.sleep(.5)
            elif (x>175 and x<475) and (y>275 and y<325):
                target = 5
                counter = 1
                time.sleep(.5)
            elif (x>175 and x<475) and (y>400 and y<450):
                target = 10
                counter = 1
                time.sleep(.5)

    
    if counter == 1:
        if extra_counter == 0:
            screen_timer(win,25,choose)
            extra_counter = 1
        win.blit(choose, (0,0))
        pygame.display.update()
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            click.play()
            if (x>0 and x<200) and (y>125 and y<550):
                player_choice = rock
                counter += 1
            elif (x>225 and x<425) and (y>125 and y<550):
                player_choice = paper
                counter += 1
            elif (x>450 and x<650) and (y>125 and y<550):
                player_choice = scissors
                counter += 1
    
    if counter == 2:
        comp_choice = random.choice([rock,paper,scissors])
        kamla(win,bg,player_score,comp_score,player_choice,comp_choice,player_area,comp_area,target)
        time.sleep(.3)
        if (player_choice == rock and comp_choice == scissors):
            player_score += 1
            kamla(win,bg,player_score,comp_score,player_choice,comp_choice,player_area,comp_area,target)
            time.sleep(.2)
            rock_s.play()
        elif (player_choice == paper and comp_choice == rock):
            player_score += 1
            kamla(win,bg,player_score,comp_score,player_choice,comp_choice,player_area,comp_area,target)
            time.sleep(.2)
            paper_s.play()
        elif (player_choice == scissors and comp_choice == paper):
            player_score += 1
            kamla(win,bg,player_score,comp_score,player_choice,comp_choice,player_area,comp_area,target)
            time.sleep(.2)
            scissors_s.play()
        elif (comp_choice == rock and player_choice == scissors):
            comp_score += 1
            kamla(win,bg,player_score,comp_score,player_choice,comp_choice,player_area,comp_area,target)
            time.sleep(.2)
            rock_s.play()
        elif (comp_choice == paper and player_choice == rock):
            comp_score += 1
            kamla(win,bg,player_score,comp_score,player_choice,comp_choice,player_area,comp_area,target)
            time.sleep(.2)
            paper_s.play()
        elif (comp_choice == scissors and player_choice == paper):
            comp_score += 1
            kamla(win,bg,player_score,comp_score,player_choice,comp_choice,player_area,comp_area,target)
            time.sleep(.2)
            scissors_s.play()
        
        counter += 1        
        time.sleep(1.75)

    if counter == 3:
        if player_score == target:
            screen_timer(win,150,won)
            counter = 4
        elif comp_score == target:
            screen_timer(win,150,lost)
            counter = 4
        else:
            counter = 1

    if counter == 4:
        win.blit(proposal,(0,0))
        pygame.display.update()
        if pygame.mouse.get_pressed()[0]:
            x,y = pygame.mouse.get_pos()
            click.play()
            if (x>225 and x<300) and (y>275 and y<400):
                extra_counter = 0
                counter = -1
                player_score = 0
                comp_score = 0
                target = 0
                player_choice = None
                comp_choice = None
            elif (x>375 and x<475) and (y>275 and y<400):
                screen_timer(win,150,thanks)
                screen_timer(win,150,code_loop)
                screen_timer(win,200,the_as8_org)
                screen_timer(win,200,poster)
                pygame.quit()
                break



pygame.quit()