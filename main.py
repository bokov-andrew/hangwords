import random, pgzero, pgzrun, os
PREFIX = 'hangman'
HANGMAN = [xx.replace('.png', '') for xx in os.listdir('images')
           if xx.startswith('hang')]
HANGMAN.sort()
HHEIGHT = Actor(HANGMAN[0]).height
HWIDTH = Actor(HANGMAN[0]).width
hpix = 0
winlose = None
words = "./words/current_spelling_words.txt"
header = "current spelling words"
# this reads in a file and then splits it by whitespace
spelling = [xx.split() for xx in open(words,"r").read().splitlines()
            # ...omitting the heading if there is one
            if xx != header]
# the above gives us a list of lists, the next line merges them to one big list
spelling = list(set(sum(spelling,[])))
ttlnumber = len(spelling)
dftnumber = 0
current_word = random.choice(spelling)
placeholder = ["_"] * len(current_word)
guessedlett = []
guessedw = []

def on_key_down(key,mod,unicode):
    global current_word, spelling, placeholder, hpix, winlose
    global guessedlett, guessedw, dftnumber
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
            # Hangman dies! (again)
            print('incorrect!')
            hpix = 0
            current_word = random.choice(spelling)
            placeholder = ["_"] * len(current_word)
            guessedlett = []
            dftnumber += 1
            winlose = 'defeat'
            
def draw():
    screen.clear()
    if winlose:
        screen.blit(winlose, (1,1))
        screen.draw.text("type any key",
                         midtop=(screen.surface.get_width()/2,
                                 screen.surface.get_height()/2),
                         fontsize=50)
    else:
        screen.blit(HANGMAN[hpix], (1,1))
        #screen.draw.text('test', (screen.surface.get_width()/2,500),fontsize=50,color=(255,0,0))
        screen.draw.text(''.join(placeholder), (20,HHEIGHT + 30))
        screen.draw.text(" ".join(guessedlett),(20,HHEIGHT + 45),
                         color = (255,0,0))
        screen.draw.text('\n'.join(guessedw), (HWIDTH + 40, 10))
        screen.draw.text(str(len(guessedw))+'/',(20,HHEIGHT + 60),color = (0,255,0))
        screen.draw.text(str(dftnumber)+'/',(40,HHEIGHT + 60),color = (255,0,0))
        screen.draw.text(str(ttlnumber),(60,HHEIGHT + 60),color = (0,0,255))
    
pgzrun.go()

