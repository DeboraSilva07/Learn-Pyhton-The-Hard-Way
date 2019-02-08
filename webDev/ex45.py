def octagon():
    print("The fight of the decade is on during UFC Fight Night 180.")
    print("You are challenging your opponent for the championship.")
    print("The fight is going into the fifth round of a championship match")
    print("and both fighters are extremely tired. The red corner (YOU) has")
    print("won rounds one and three but the blue corner has won rounds two and")
    print("four. You notice that your opponent's head is bleeding and badly brused.")
    print("The round has now started and for respect you give each other a fist bump.")
    print("What do you first? (punch, kick, or dodge)(these are the only choices for now due to simplicity)")
    first_choice()
    
def first_choice():
    choice = input("> ")
    
    if "punch" in choice.lower():
        print("You throw a right hook and your opponent dodges your punch.")
        print("He comes up and gives you an uppercut that stuns you.")
        print("What is your next move?")
        second_choice()
        
    elif "kick" in choice.lower():
        print("You kick your opponent in the leg and he lets out a grunt of pain.")
        print("What is your next move?")
        second_choice()
    
    elif "dodge" in choice.lower():
        print("The opponent swings a left hook and you sway under the punch.")
        print("What is your next move?")
        second_choice()
        
    else:
        print("I got no idea what that means.")


def second_choice():
    choice = input("> ")    
    
    if "punch" in choice.lower():
        print("""
        You go for a left jab then an uppercut combo and make your
        opponent stumble to the ground but he quickly gets back up.
        What is your next move?
        """)
        third_choice()
    
    elif "kick" in choice.lower():
        print("""
        You go for a body kick and your opponent catches the kick and gives you 
        a right stright to your face and you fall but quickly get back up
        What is your next move?
        """)
        third_choice()
        
    elif "dodge" in choice.lower():
        print("""
        You dodge a spinning head kick and hit him in the kidney. This hit completely 
        drains his energy and you swing a right overhead punch and knock him to the ground.
        What is your next move (Ground and Pound, Submission attempt, Let him get up)
        """)
        dodge_choice()
        
    else:
        print("I got no idea what that means.")
    

def third_choice():
    choice = input("> ")  
    
    if "punch" in choice.lower():
        print("""
        You go for a left overhand and you hit him right in the nose.
        You felt his nose crack and he goes down unconsious and the 
        ref signals for the match to end.
        """)
        win()
        
        
    if "kick" in choice.lower():
        print("""
        You get an adrenaline rush and you put all your energy into a 
        spinning head kick. You spin and swing your leg but you don't 
        feel a connection to his head. You look back at the opponent 
        and he ducked your head kick attempt and he powerfully hits you 
        in the kidney and you fall to the ground in agonizing pain.
        """)
        lose()
        
    else:
            print("I got no idea what that means.")    



def dodge_choice():
    choice = input("> ")
    
    if "ground and pound" in choice.lower():
        print("""
        You dive on top of him (pause) and go crazy with your punching and your elbows.
        You keep punching then you see that he goes unconsious. The ref pushes you off of
        him and he signals for the fight to stop.
        """)
        win()
    
    elif "submission attempt" in choice.lower():
        print("""
        You go on the ground and go for a Japanese Necktie submission hold.
        You have him in the perfect position and he is starting to fade away.
        The ref is yelling for him to signal that he is still consious and
        he does not respond. The ref pushes you off of him and he signals for 
        the fight to stop.
        """)
        win()
    
    elif "let" in choice.lower():
        print("""
        Your opponent gets up and you gets an angry look in his eye. He limps toward you 
        while you're breathing heavily and he starts swinging left and right hooks. A right
        hook lands right on your temple and you black out. You wake up to a medical team 
        surrounding you.
        """)
        dodge_lose()
        
    else:
        print("I got no idea what that means.")    
        

def win():
    print("""You are now the Greatest Of All Time winning both championships in the middleweight
    division and the light heavy weight division.""")
    exit(0)



def lose():
    print("""
    Welp, you got knocked the *bleep* out HAHA.
    """)
    exit(0)



def dodge_lose():
    print("""
    You have suffered a fractured skull and most likely have CTE now.
    This should teach you that when you have the opportunity to win,
    take it in any way possible.
    """)
    exit(0)


        
octagon()