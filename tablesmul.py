### Section des imports
import random

### Section des constantes
Q_TEST = (4, 6)
PATRON_Q = "Combien font %s x %s ? "
MINI = 1
MAXI = 12
Q_MAX = 4

### Sections des fonctions
def creer_listeq(nmin = MINI, nmax = MAXI, hasard=True):
    tempo = [(x+1, y+1) for x in range(nmin-1, nmax)
                        for y in range(nmin-1, nmax)]
    if hasard is True:
        random.shuffle(tempo)
    return(tempo)

def faire_test():
    liste_q = creer_listeq()
    score = 0
    for i, question in enumerate(liste_q):
        if i >= Q_MAX:
            break
        invite = PATRON_Q%question
        repon_ok = question[0]*question[1]
        repon_saisie = input(invite)
        
        if int(repon_saisie)== repon_ok:
            print("Correct !")
            score = score+1
        else:
            print("Incorrect, c'était %s."%(repon_ok))

    print("Nombre de calculs corrects : %s"%score)

faire_test()
