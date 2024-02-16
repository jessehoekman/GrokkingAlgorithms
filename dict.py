voted = {}

def check_voter(name):
    if voted.get(name):
        print("kick out retard!")
    else:
        voted[name] = True
        print ("let retard vote ;)))")

print(check_voter("Tom"))
print(check_voter("Tom"))

print(voted)
