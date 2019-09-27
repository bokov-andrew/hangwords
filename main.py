import random, pgzero, pgzrun, os
PREFIX = 'hangman'
HANGMAN = [xx.replace('.png', '') for xx in os.listdir('images') if xx.startswith('hang')]
HANGMAN.sort()
HHEIGHT = Actor(HANGMAN[0]).height
HWIDTH = Actor(HANGMAN[0]).width
hpix = 0
winlose = None
words = "./words/current_spelling_words.txt"
spelling = open(words, "r").read().splitlines()[1:]
spelling = list(set(spelling))
current_word = random.choice(spelling)
placeholder = ["_"] * len(current_word)
guessedlett = []
guessedw = []

def on_key_down(key,mod,unicode):
    global current_word, spelling, placeholder, hpix, winlose, guessedlett, guessedw
    if winlose:
        winlose = None
    elif unicode in current_word: # if you guessed right
        letrlocate = [kk for kk,vv in enumerate(current_word) if vv == unicode]
        for ii in letrlocate:
            placeholder[ii] = unicode
      #  screen.draw.text('Yes!',(30,120), background = "blue")
        if current_word == "".join(placeholder):
            # This triggers when you guessed the whole word
            hpix = 0
            spelling.remove(current_word)
            guessedw += [current_word]
            if spelling:
                current_word = random.choice(spelling)
                placeholder = ["_"] * len(current_word)
                guessedlett = []
                winlose = 'victory'
            else:
                print("w00t")
                return()
    else: # if you guessed wrong...
        hpix += 1
        guessedlett += [unicode]
        if hpix == len (HANGMAN):
            print('incorrect!')
            hpix = 0
            current_word = random.choice(spelling)
            placeholder = ["_"] * len(current_word)
            guessedlett = []
            winlose = 'defeat'
            
def draw():
    screen.clear()
    if winlose:
        screen.blit(winlose, (1,1))
    else:
        screen.blit(HANGMAN[hpix], (1,1))
    #screen.draw.text(current_word, (20,HHEIGHT + 10))
    screen.draw.text(''.join(placeholder), (20,HHEIGHT + 30))
    screen.draw.text(" ".join(guessedlett),(20,HHEIGHT + 45),
                     color = (255,0,0))
    screen.draw.text('\n'.join(guessedw), (HWIDTH + 40, 10))
    
pgzrun.go()

