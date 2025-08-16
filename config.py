SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
screen = None

gravity = 8
gameOver = False
distance = 0

#BACKGROUND
groundHeight = 100
cacti = []
birds = []
cactiSpeed = 8
maxCactiSpeed = 15
cactusImage = None
birdImage = None
cactusWidth, cactusHeight = None, None
birdWidth, birdHeight = None, None

#DINO
runningDinoHeight = None
duckingDinoHeight = None
dinoWidth, dinoHeight = None, 80
dinoPos = None
dinoVel = (0, 0)
jumping = False
ducking = False
jumpStrength = 50