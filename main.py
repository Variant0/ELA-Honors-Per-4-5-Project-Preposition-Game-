import pygame
import question_list
from pygame.locals import KEYDOWN, K_BACKSPACE, K_RETURN, K_SPACE
import random
from typing import Optional, Tuple

# Initialize pygame module & set up screen
pygame.init()
screen = pygame.display.set_mode([500, 700])

p1name = p2name = ""
input_active = 0  # Flag to track the input stage (0 for player 1, 1 for player 2, 2 for finished)
game_stage = 0  # Flag for the phase of the game
# Pygame loop

lp0 = lp1 = lp2 = lp3 = lp4 = True

p1score = p2score = 0
ans_pos = ans_pos_p2 = 0

# Original versions, can be used to restore editables
possible_positions_p1_orig = [(195, 180), (375, 180), (195, 260), (375, 260)]
possible_positions_p2_orig = [(195, 530), (375, 530), (195, 610), (375, 610)]

# Editable versions
possible_positions_p1_edb = [(195, 180), (375, 180), (195, 260), (375, 260)]
possible_positions_p2_edb = [(195, 530), (375, 530), (195, 610), (375, 610)]


def display_text(t: str, x: int, y: int, sz: int, ftype: Optional[str] = None) -> None:
    pfont = pygame.font.SysFont(ftype, sz)
    txtsrf = pfont.render(t, True, (0, 0, 0))
    txtrec = txtsrf.get_rect(center=(x, y))
    screen.blit(txtsrf, txtrec)


def draw_rect_skeleton(point1: Tuple[int, int],
                       point2: Tuple[int, int],
                       point3: Tuple[int, int],
                       point4: Tuple[int, int],
                       color: Tuple[int, int, int],
                       width: int) -> None:
    pygame.draw.line(screen, color, point1, point2, width)
    pygame.draw.line(screen, color, point2, point3, width)
    pygame.draw.line(screen, color, point3, point4, width)
    pygame.draw.line(screen, color, point4, point1, width)


def generate_question() -> question_list.Question:
    rnd_index = random.randint(0, 29)
    question = question_list.question_list[rnd_index]
    return question


question_p1: question_list.Question = generate_question()
question_p2: question_list.Question = generate_question()

random.shuffle(possible_positions_p1_edb)
random.shuffle(possible_positions_p2_edb)

lc1 = possible_positions_p1_edb[0]
lc2 = possible_positions_p1_edb[1]
lc3 = possible_positions_p1_edb[2]
lc4 = possible_positions_p1_edb[3]

lc1b = possible_positions_p2_edb[0]
lc2b = possible_positions_p2_edb[1]
lc3b = possible_positions_p2_edb[2]
lc4b = possible_positions_p2_edb[3]

wr_an1, wr_an2, wr_an3 = question_p1.get_arg_wr_ans()
wr_an1b, wr_an2b, wr_an3b = question_p2.get_arg_wr_ans()


while lp0:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lp0 = False
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                lp0 = False

    display_text("Welcome to ", 250, 100, 30)
    display_text("VERBAL VERSUS", 250, 300, 70, "Arial")
    display_text("Press enter to begin", 250, 500, 20)

    pygame.display.flip()

screen.fill((255, 255, 255))

while lp1:

    # ------------------------------------- INPUT PHASE -----------------------------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lp1 = False
            exit(0)

        if input_active == 2:
            lp1 = False

        # Player 1 name input
        if event.type == KEYDOWN and input_active == 0:
            if event.key == K_BACKSPACE:
                p1name = p1name[:-1]
            elif event.key == K_SPACE:
                if len(p1name) < 20:
                    p1name += ' '
            elif event.key == K_RETURN:
                if p1name:  # Only move on if player 1's name is not empty
                    input_active = 1
            elif len(p1name) < 20:
                # Allow letters and digits only
                if event.unicode.isalpha() or event.unicode.isdigit():
                    mods = pygame.key.get_mods()
                    if mods & pygame.KMOD_SHIFT:
                        p1name += event.unicode.upper()
                    else:
                        p1name += event.unicode

        # Player 2 name input
        elif event.type == KEYDOWN and input_active == 1:
            if event.key == K_BACKSPACE:
                p2name = p2name[:-1]
            elif event.key == K_SPACE:
                if len(p2name) < 20:
                    p2name += ' '
            elif event.key == K_RETURN:
                if p2name:  # Only finish input if player 2's name is not empty
                    input_active = 2  # Input for both players is done
            elif len(p2name) < 20:
                if event.unicode.isalpha() or event.unicode.isdigit():
                    mods = pygame.key.get_mods()
                    if mods & pygame.KMOD_SHIFT:
                        p2name += event.unicode.upper()
                    else:
                        p2name += event.unicode

    # Function to display text on the screen

    # Clear screen
    screen.fill((255, 255, 255))

    # Display instructions for input
    if input_active == 0:
        display_text("Enter the first player's name:", 250, 50, 30)
    elif input_active == 1:
        display_text("Enter the second player's name:", 250, 50, 30)
    elif input_active == 2:
        game_stage = 1

    # Display the entered names
    display_text(f"Player 1: {p1name}", 250, 100, 30)
    if input_active > 0:
        display_text(f"Player 2: {p2name}", 250, 150, 30)

    # Update the display
    pygame.display.flip()

while lp2:
    # ----------------------------------- HOW TO PLAY (in game explanation) ------------------------------------
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lp2 = False
            exit(0)
        if event.type == KEYDOWN:
            if event.key == pygame.K_RETURN:
                lp2 = False

    display_text("How this game works:", 250, 100, 30)
    display_text("Two people will be racing to get to 15 questions", 250, 130, 30)
    display_text("correct.", 250, 160, 30)
    display_text(f"Player one ({p1name}) will be using the keys", 250, 190, 30)
    display_text(" 1, 2, 3, and 4 to answer their questions.", 250, 220, 30)
    display_text(f"Player two ({p2name}) will be using the keys", 250, 250, 30)
    display_text("7, 8, 9, and 0 to answer their questions.", 250, 280, 30)
    display_text(f"{p1name} and {p2name},", 250, 450, 30)
    display_text("When you are ready, press enter.", 250, 500, 30)

    pygame.display.flip()

while lp3:
    # ------------------------------------------ MAIN GAME -----------------------------------------------------
    screen.fill((255, 255, 255))

    pygame.draw.line(screen, (0, 0, 0), (0, 350), (500, 350), width=5)

    # Player 1 stuff
    # Displaying P1 name
    display_text(f"{p1name}", 250, 30, 20)
    # Question box
    draw_rect_skeleton((120, 50), (450, 50), (450, 130), (120, 130), (0, 0, 0), 2)
    # Answer boxes
    display_text("1", 195, 145, 15)
    draw_rect_skeleton((120, 150), (270, 150), (270, 220), (120, 220), (0, 0, 0), 2)
    display_text("2", 375, 145, 15)
    draw_rect_skeleton((120, 230), (270, 230), (270, 300), (120, 300), (0, 0, 0), 2)
    display_text("3", 195, 226, 15)
    draw_rect_skeleton((300, 150), (450, 150), (450, 220), (300, 220), (0, 0, 0), 2)
    display_text("4", 375, 226, 15)
    draw_rect_skeleton((300, 230), (450, 230), (450, 300), (300, 300), (0, 0, 0), 2)
    # Question Bar (Shows how questions you got correct)
    draw_rect_skeleton((50, 300), (50, 50), (100, 50), (100, 300), (0, 0, 0), 2)

    # Player 2 stuff
    # Displaying P2 name
    display_text(f"{p2name}", 250, 380, 20)
    # Question box
    draw_rect_skeleton((120, 400), (450, 400), (450, 480), (120, 480), (0, 0, 0), 2)
    # Answer boxes
    display_text("7", 195, 495, 15)
    draw_rect_skeleton((120, 500), (270, 500), (270, 570), (120, 570), (0, 0, 0), 2)
    display_text("8", 375, 495, 15)
    draw_rect_skeleton((120, 580), (270, 580), (270, 650), (120, 650), (0, 0, 0), 2)
    display_text("9", 195, 577, 15)
    draw_rect_skeleton((300, 500), (450, 500), (450, 570), (300, 570), (0, 0, 0), 2)
    display_text("0", 375, 577, 15)
    draw_rect_skeleton((300, 580), (450, 580), (450, 650), (300, 650), (0, 0, 0), 2)
    # Question Bar
    draw_rect_skeleton((50, 650), (50, 400), (100, 400), (100, 650), (0, 0, 0), 2)

    # Displaying Questions & Possible Answers for player 1
    display_text(question_p1.get_arg_question(), 267, 65, 20, "Arial")
    display_text(question_p1.get_arg_ans(), lc1[0], lc1[1], 25)
    display_text(wr_an1, lc2[0], lc2[1], 25)
    display_text(wr_an2, lc3[0], lc3[1], 25)
    display_text(wr_an3, lc4[0], lc4[1], 25)

    # Displaying Questions & Possible Answers for player 2
    display_text(question_p2.get_arg_question(), 267, 415, 20, "Arial")
    display_text(question_p2.get_arg_ans(), lc1b[0], lc1b[1], 25)
    display_text(wr_an1b, lc2b[0], lc2b[1], 25)
    display_text(wr_an2b, lc3b[0], lc3b[1], 25)
    display_text(wr_an3b, lc4b[0], lc4b[1], 25)

    # Event reader
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lp3 = False
            exit(0)

        if event.type == KEYDOWN:
            if event.key == pygame.K_1:
                if lc1 == possible_positions_p1_orig[0]:
                    p1score = p1score + 1
                else:
                    p1score = 0

                question_p1 = generate_question()
                random.shuffle(possible_positions_p1_edb)
                lc1 = possible_positions_p1_edb[0]
                lc2 = possible_positions_p1_edb[1]
                lc3 = possible_positions_p1_edb[2]
                lc4 = possible_positions_p1_edb[3]
                wr_an1, wr_an2, wr_an3 = question_p1.get_arg_wr_ans()

            elif event.key == pygame.K_2:
                if lc1 == possible_positions_p1_orig[1]:
                    p1score = p1score + 1
                else:
                    p1score = 0

                question_p1 = generate_question()
                random.shuffle(possible_positions_p1_edb)
                lc1 = possible_positions_p1_edb[0]
                lc2 = possible_positions_p1_edb[1]
                lc3 = possible_positions_p1_edb[2]
                lc4 = possible_positions_p1_edb[3]
                wr_an1, wr_an2, wr_an3 = question_p1.get_arg_wr_ans()

            elif event.key == pygame.K_3:
                if lc1 == possible_positions_p1_orig[2]:
                    p1score = p1score + 1
                else:
                    p1score = 0

                question_p1 = generate_question()
                random.shuffle(possible_positions_p1_edb)
                lc1 = possible_positions_p1_edb[0]
                lc2 = possible_positions_p1_edb[1]
                lc3 = possible_positions_p1_edb[2]
                lc4 = possible_positions_p1_edb[3]
                wr_an1, wr_an2, wr_an3 = question_p1.get_arg_wr_ans()

            elif event.key == pygame.K_4:
                if lc1 == possible_positions_p1_orig[3]:
                    p1score = p1score + 1
                else:
                    p1score = 0

                question_p1 = generate_question()
                random.shuffle(possible_positions_p1_edb)
                lc1 = possible_positions_p1_edb[0]
                lc2 = possible_positions_p1_edb[1]
                lc3 = possible_positions_p1_edb[2]
                lc4 = possible_positions_p1_edb[3]
                wr_an1, wr_an2, wr_an3 = question_p1.get_arg_wr_ans()

            if event.key == pygame.K_7:
                if lc1b == possible_positions_p2_orig[0]:
                    p2score = p2score + 1
                else:
                    p2score = 0

                question_p2 = generate_question()
                random.shuffle(possible_positions_p2_edb)
                lc1b = possible_positions_p2_edb[0]
                lc2b = possible_positions_p2_edb[1]
                lc3b = possible_positions_p2_edb[2]
                lc4b = possible_positions_p2_edb[3]
                wr_an1b, wr_an2b, wr_an3b = question_p2.get_arg_wr_ans()

            elif event.key == pygame.K_8:
                if lc1b == possible_positions_p2_orig[1]:
                    p2score = p2score + 1
                else:
                    p2score = 0

                question_p2 = generate_question()
                random.shuffle(possible_positions_p2_edb)
                lc1b = possible_positions_p2_edb[0]
                lc2b = possible_positions_p2_edb[1]
                lc3b = possible_positions_p2_edb[2]
                lc4b = possible_positions_p2_edb[3]
                wr_an1b, wr_an2b, wr_an3b = question_p2.get_arg_wr_ans()

            elif event.key == pygame.K_9:
                if lc1b == possible_positions_p2_orig[2]:
                    p2score = p2score + 1
                else:
                    p2score = 0

                question_p2 = generate_question()
                random.shuffle(possible_positions_p2_edb)
                lc1b = possible_positions_p2_edb[0]
                lc2b = possible_positions_p2_edb[1]
                lc3b = possible_positions_p2_edb[2]
                lc4b = possible_positions_p2_edb[3]
                wr_an1b, wr_an2b, wr_an3b = question_p2.get_arg_wr_ans()

            elif event.key == pygame.K_0:
                if lc1b == possible_positions_p2_orig[3]:
                    p2score = p2score + 1
                else:
                    p2score = 0

                question_p2 = generate_question()
                random.shuffle(possible_positions_p2_edb)
                lc1b = possible_positions_p2_edb[0]
                lc2b = possible_positions_p2_edb[1]
                lc3b = possible_positions_p2_edb[2]
                lc4b = possible_positions_p2_edb[3]
                wr_an1b, wr_an2b, wr_an3b = question_p2.get_arg_wr_ans()

    if p1score >= 15 or p2score >= 15:
        lp3 = False

    else:
        for idx in range(p1score):
            pygame.draw.rect(screen, (0, 0, 255), [51, 285 - (16.6 * idx), 50, 20])

        for idx in range(p2score):
            pygame.draw.rect(screen, (0, 0, 255), [51, 635 - (16.6 * idx), 50, 20])

    pygame.display.flip()

while lp4:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lp4 = False
            exit(0)

    if p1score >= 15:
        display_text(f"{p1name} wins!", 200, 200, 100, "Arial")
    else:
        display_text(f"{p2name} wins!", 200, 200, 100, "Arial")

    pygame.display.flip()

pygame.quit()
