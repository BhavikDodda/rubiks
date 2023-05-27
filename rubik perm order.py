import random
from math import gcd
def main(moves):
    rubikfunc=constructIdentity()
    shuffle(rubikfunc,moves)

    cycles=[]
    func=rubikfunc.copy() #is a bijective function
    print('\nbijective function: ',func)
    keys=func.keys()
    toggle=dict(zip(keys, [None]*len(keys)))

    check=[(key,val) for key,val in toggle.items() if val==None]
    cycle=[]
    curr=check[0][0]
    while (len(check)>0):
        if (toggle[curr]==None):
            cycle.append(curr)
            toggle[curr]=1
            curr=func[curr]
        else:
            cycles.append(cycle)
            check=[(key,val) for key,val in toggle.items() if val==None]
            cycle=[]
            curr=check[0][0] if len(check)>0 else curr
    print('\ncycle notation: ',cycles)

    #finding order
    lcm = 1
    for i in cycles:
        j=len(i)
        lcm = lcm*j//gcd(lcm, j)
    return(lcm)

def constructIdentity():
    cdict={}
    for j in ['u','d','l','r','f','b']:
        for i in range(9):
            cdict[j+str(i+1)]=j+str(i+1)
    return cdict

#base functions to easily define rotation
def faceplane_rot(perm,face,sign):
    if sign==1:
        perm[face+'1'],perm[face+'2'],perm[face+'3'],perm[face+'4'],perm[face+'6'],perm[face+'7'],perm[face+'8'],perm[face+'9']=perm[face+'3'],perm[face+'6'],perm[face+'9'],perm[face+'2'],perm[face+'8'],perm[face+'1'],perm[face+'4'],perm[face+'7']
    else:
        perm[face+'1'],perm[face+'2'],perm[face+'3'],perm[face+'4'],perm[face+'6'],perm[face+'7'],perm[face+'8'],perm[face+'9']=perm[face+'7'],perm[face+'4'],perm[face+'1'],perm[face+'8'],perm[face+'2'],perm[face+'9'],perm[face+'6'],perm[face+'3']

def nonfaceplane_rot(perm,facearray,sign):
    fa=facearray
    if sign==1:
        perm[fa[0][0]+fa[0][1]],perm[fa[0][0]+fa[0][2]],perm[fa[0][0]+fa[0][3]], perm[fa[1][0]+fa[1][1]],perm[fa[1][0]+fa[1][2]],perm[fa[1][0]+fa[1][3]], perm[fa[2][0]+fa[2][1]],perm[fa[2][0]+fa[2][2]],perm[fa[2][0]+fa[2][3]], perm[fa[3][0]+fa[3][1]],perm[fa[3][0]+fa[3][2]],perm[fa[3][0]+fa[3][3]] = perm[fa[3][0]+fa[3][1]],perm[fa[3][0]+fa[3][2]],perm[fa[3][0]+fa[3][3]] , perm[fa[0][0]+fa[0][1]],perm[fa[0][0]+fa[0][2]],perm[fa[0][0]+fa[0][3]], perm[fa[1][0]+fa[1][1]],perm[fa[1][0]+fa[1][2]],perm[fa[1][0]+fa[1][3]], perm[fa[2][0]+fa[2][1]],perm[fa[2][0]+fa[2][2]],perm[fa[2][0]+fa[2][3]]
    else:
        perm[fa[0][0]+fa[0][1]],perm[fa[0][0]+fa[0][2]],perm[fa[0][0]+fa[0][3]], perm[fa[1][0]+fa[1][1]],perm[fa[1][0]+fa[1][2]],perm[fa[1][0]+fa[1][3]], perm[fa[2][0]+fa[2][1]],perm[fa[2][0]+fa[2][2]],perm[fa[2][0]+fa[2][3]], perm[fa[3][0]+fa[3][1]],perm[fa[3][0]+fa[3][2]],perm[fa[3][0]+fa[3][3]] = perm[fa[1][0]+fa[1][1]],perm[fa[1][0]+fa[1][2]],perm[fa[1][0]+fa[1][3]], perm[fa[2][0]+fa[2][1]],perm[fa[2][0]+fa[2][2]],perm[fa[2][0]+fa[2][3]], perm[fa[3][0]+fa[3][1]],perm[fa[3][0]+fa[3][2]],perm[fa[3][0]+fa[3][3]] , perm[fa[0][0]+fa[0][1]],perm[fa[0][0]+fa[0][2]],perm[fa[0][0]+fa[0][3]]
#shuffle
def shuffle(perm,arr):
    movelist=['r','rp','l','lp','u','up','d','dp','f','fp','b','bp']
    moveaction=[[['f','9','6','3'],['u','9','6','3'],['b','1','4','7'],['d','9','6','3']],[['f','7','4','1'],['u','7','4','1'],['b','3','6','9'],['d','7','4','1']],[['f','3','2','1'],['l','3','2','1'],['b','3','2','1'],['r','3','2','1']],[['f','9','8','7'],['l','9','8','7'],['b','9','8','7'],['r','9','8','7']],[['u','7','8','9'],['r','1','4','7'],['d','3','2','1'],['l','9','6','3']],[['u','1','2','3'],['r','3','6','9'],['d','9','8','7'],['l','7','4','1']]]
    for i in reversed(arr): #function composition from right to left
        if i in movelist:
            parity=(-1 if 'p' in i else 1)
            faceplane_rot(perm,i[0],parity)

            parity2=(parity+1)//2-1
            pairIndex=(parity2+movelist.index(i))//2
            nonfaceplane_rot(perm,moveaction[pairIndex],(2*(pairIndex%2)-1)*parity)      

if __name__ == '__main__':
    moves=list(map(str, input("moves: ").strip().split()))
    ans=main(moves)
    print(f"\nOrder of permutation: {ans}\n")
