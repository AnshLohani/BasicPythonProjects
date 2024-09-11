import random

words = [
    "apple", "banana", "orange", "pear", "grape",
    "strawberry", "blueberry", "raspberry", "blackberry", "cherry",
    "lemon", "lime", "mango", "kiwi", "avocado",
    "watermelon", "honeydew", "cantaloupe", "pineapple", "papaya",
    "plum", "peach", "nectarines", "apricot", "fig",
    "date", "pomegranate", "coconut", "olive", "nut",
    "bread", "butter", "milk", "cheese", "egg",
    "meat", "fish", "chicken", "beef", "pork",
    "rice", "pasta", "potato", "corn", "beans",
    "carrot", "celery", "onion", "garlic", "pepper",
    "tomato", "cucumber", "lettuce", "spinach", "broccoli",
    "cabbage", "zucchini", "squash", "green beans", "asparagus",
    "mushroom", "olives", "pickle", "sausage", "bacon",
    "ham", "hotdog", "burger", "pizza", "sandwich",
    "soup", "salad", "steak", "sushi", "taco",
    "burrito", "quesadilla", "spaghetti", "lasagna", "ramen",
    "pancake", "waffle", "toast", "cereal", "yogurt",
    "ice cream", "cookie", "cake", "pie", "candy",
    "chocolate", "popcorn", "chips", "soda", "juice",
    "water", "tea", "coffee", "wine", "beer",
    "car", "truck", "bus", "bike", "motorcycle",
    "airplane", "boat", "train", "helicopter", "rocket",
    "house", "apartment", "hotel", "cabin", "tent",
    "school", "hospital", "library", "museum", "park",
    "beach", "forest", "mountain", "river", "lake",
    "ocean", "desert", "island", "city", "country",
    "dog", "cat", "horse", "bird", "fish",
    "rabbit", "monkey", "elephant", "lion", "tiger",
    "bear", "deer", "wolf", "fox", "squirrel",
    "snake", "turtle", "frog", "lizard", "butterfly",
    "bee", "ant", "spider", "worm", "grasshopper",
    "mouse", "rat", "hamster", "guinea pig", "goldfish",
    "computer", "phone", "tablet", "laptop", "TV",
    "radio", "camera", "watch", "clock", "calculator",
    "keyboard", "mouse", "printer", "scanner", "speaker",
    "book", "magazine", "newspaper", "comic book", "dictionary",
    "encyclopedia", "novel", "poetry", "essay", "letter",
    "email", "text message", "website", "blog", "forum",
    "game", "toy", "puzzle", "board game", "video game",
    "movie", "TV show", "music", "song", "album",
    "artist", "band", "singer", "musician", "guitar",
    "piano", "drums", "violin", "cello", "flute",
    "trumpet", "saxophone", "clarinet", "bass", "ukulele",
    "color", "shape", "size", "number", "letter",
    "word", "sentence", "paragraph", "story", "book",
    "chapter", "page", "line", "word", "letter"
]

def rword():
    rword = random.sample(words,1)
    x = rword[0].lower()
    return x


finalword = rword()
g = list()
t=-1

print("First try free!")
while True:
    guess = input("enter a letter (A-Z): ")
    if t == 10:
        print("Game Over!")
        print(f"The word was {finalword}")
        continue
    if len(guess) != 1:
        print("Enter only one letter!")
        continue
    else:
        if guess in g:
            print("Already Guessed before! Try Again :)")
            continue
        else:
            t+=1
            g.append(guess)
            guessword= ''        
            for i in finalword:
                if i in g:
                    guessword += f'{i}'
                elif i == ' ':
                    guessword += ' '
                else:
                    guessword += '_'
            print(guessword)

            if guessword == finalword:
                print(f"Yay! You Guessed it!It only took you {t} tries")
                print(guessword)
                ch = input("Play again? (y/n):  ")
                if ch.lower() == 'n':
                    break
                else:
                    finalword = rword()
                    t=-1
                    print("First try free!")
                    g = list()
            

        




