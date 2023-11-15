#Makai Moody-Broen
#HW 2


print('You are in a strange wood. Paths lead [e]ast and [w]est')
print('Which path will you take')
path1 = input()
has_key = False
has_rock = False
if path1 == 'e':
    print('in a patch of grass you find a rock')
    has_rock = True
elif path1 == 'w':
    print('you find an old fire pit with a key inside')
    has_key = True

print('You arrive at a lonely beach')
print('Continue along [b]each or head [i]nland')
path2 = input()
if path2 =='b':
    pass
elif path2 =='i':
    print('the ground is very marshy and walking has become tiresome')
    print('return to [b]each or [c]ontinue onwards')
    path3 = input()
    if path3 == 'b':
        pass
    elif path3== 'c':
        print('the water rises as you continue your trek, you succumb to the pull of the water and fall head first into the feeding ground')
        print('Game Over')
        quit()


print('The beach appears endless in all directions, as you continue the effects of dehydraytion set in. The only water around is brackish, but after an hour of walking you stumble upon a locked shack')
if has_key == True:
    print('Will you try the key on the door? [y/n]')
    path4 = input()
    if path4 == 'y':
        print('The key unlocks the door to the shack')
    elif path4 == 'n':
        print('Out of either a sense of deep seeded cowardice or perhaps dignified respect, you turn your back on the looming structure. You make your way to the highway, and eventually rejoin society')
        print('Game over')
        quit()
elif has_rock == True:
    print('Will you use the [r]ock to batter the lock of the strange hut or will you [l]eave')
    path5 = input()
    if path5 == 'r':
        print('you violently assault the mechanism barring the door, eventually the lock splinters and thuds to the earth, you stumble off balance into the dark precipice of the unknown')
    elif path5 == 'l':
        print('Out of either a sense of deep seeded cowardice or perhaps dignified respect, you turn your back on the looming structure. You make your way to the highway, and eventually rejoin society')
        print('Game over')
        quit()

print('Inside the shack a man sits bathed in shadow. He utters no words and gives no answers, but as though he can percieve your desires he brings forth a small container of what seems to be water')
print('Do you accept the container? [y/n]')
path6 = input()
if path6 == 'y':
    print('will you [d]rink the contents or [p]our the liquid into the earth')
    path7 = input()
    if path7 == 'd':
        print('You smell the putrid vapor of the conction before the taste begins to bloom upon your tounge. Your vision begins to fog as you catch a last look of the mans face. You feel your knees give out and you are bombarded by the strange sense that reality itself is slipping away.')
        print('You awake in the ruins of what once was the old mans shack. The air feels heavier and your surroundings seem almost alien. Many years later, once you have adjusted to the apoclyptic lifestlye of the distant future, the thin smile parsed upon the strange mans lips still lingers in your mind')
        print('Game Over')
        quit()
    elif path7 == 'p':
        print('The contents of the bottle assault the earth. The distinct smell of sulfur burns at your senses and the room comes alive with vapor')
        print('The last glimpse you catch is that of the old mans scowl, when you awaken the old man is gone')
        print('Game Over')
        quit()

elif path6 == 'n':
    print('You turn your back on the strange mans outstretched hand. You eventually stumble back to the clutches of safety. The eery aurora and the half cloaked face of the man in the cabin never leave your mind, and to this day you reamin haunted by indecision')
    print('Game Over')
    quit()





