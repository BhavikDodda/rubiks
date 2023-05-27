import random
from math import gcd
def main(moves):
    """n=10
    s=list(range(n))
    random.shuffle(s)
    rubikfunc=dict([(str(i),str(s[i])) for i in range(n)])"""
    rubikfunc={"u1":"u1","u2":"u2","u3":"u3","u4":"u4","u5":"u5","u6":"u6","u7":"u7","u8":"u8","u9":"u9",
               "d1":"d1","d2":"d2","d3":"d3","d4":"d4","d5":"d5","d6":"d6","d7":"d7","d8":"d8","d9":"d9",
               "l1":"l1","l2":"l2","l3":"l3","l4":"l4","l5":"l5","l6":"l6","l7":"l7","l8":"l8","l9":"l9",
               "r1":"r1","r2":"r2","r3":"r3","r4":"r4","r5":"r5","r6":"r6","r7":"r7","r8":"r8","r9":"r9",
               "f1":"f1","f2":"f2","f3":"f3","f4":"f4","f5":"f5","f6":"f6","f7":"f7","f8":"f8","f9":"f9",
               "b1":"b1","b2":"b2","b3":"b3","b4":"b4","b5":"b5","b6":"b6","b7":"b7","b8":"b8","b9":"b9"}
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


    lcm = 1
    for i in cycles:
        j=len(i)
        lcm = lcm*j//gcd(lcm, j)
    return(lcm)

def rotate_r(perm):
    faceplane_rot(perm,'r',1)
    nonfaceplane_rot(perm,[['f','9','6','3'],['u','9','6','3'],['b','1','4','7'],['d','9','6','3']],-1)
def rotate_rp(perm):
    faceplane_rot(perm,'r',-1)
    nonfaceplane_rot(perm,[['f','9','6','3'],['u','9','6','3'],['b','1','4','7'],['d','9','6','3']],1)
def rotate_l(perm):
    faceplane_rot(perm,'l',1)
    nonfaceplane_rot(perm,[['f','7','4','1'],['u','7','4','1'],['b','3','6','9'],['d','7','4','1']],1)
def rotate_lp(perm):
    faceplane_rot(perm,'l',-1)
    nonfaceplane_rot(perm,[['f','7','4','1'],['u','7','4','1'],['b','3','6','9'],['d','7','4','1']],-1)
def rotate_u(perm):
    faceplane_rot(perm,'u',1)
    nonfaceplane_rot(perm,[['f','3','2','1'],['l','3','2','1'],['b','3','2','1'],['r','3','2','1']],-1)
def rotate_up(perm):
    faceplane_rot(perm,'u',-1)
    nonfaceplane_rot(perm,[['f','3','2','1'],['l','3','2','1'],['b','3','2','1'],['r','3','2','1']],1)
def rotate_d(perm):
    faceplane_rot(perm,'d',1)
    nonfaceplane_rot(perm,[['f','9','8','7'],['l','9','8','7'],['b','9','8','7'],['r','9','8','7']],1)
def rotate_dp(perm):
    faceplane_rot(perm,'d',-1)
    nonfaceplane_rot(perm,[['f','9','8','7'],['l','9','8','7'],['b','9','8','7'],['r','9','8','7']],-1)
def rotate_f(perm):
    faceplane_rot(perm,'f',1)
    nonfaceplane_rot(perm,[['u','7','8','9'],['r','1','4','7'],['d','3','2','1'],['l','9','6','3']],-1)
def rotate_fp(perm):
    faceplane_rot(perm,'f',-1)
    nonfaceplane_rot(perm,[['u','7','8','9'],['r','1','4','7'],['d','3','2','1'],['l','9','6','3']],1)
def rotate_b(perm):
    faceplane_rot(perm,'b',1)
    nonfaceplane_rot(perm,[['u','1','2','3'],['r','3','6','9'],['d','9','8','7'],['l','7','4','1']],1)
def rotate_bp(perm):
    faceplane_rot(perm,'b',-1)
    nonfaceplane_rot(perm,[['u','1','2','3'],['r','3','6','9'],['d','9','8','7'],['l','7','4','1']],-1)
#base functions to make things easier
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
    for i in reversed(arr): #function composition from right to left
        if i in ['r','rp','l','lp','u','up','d','dp','f','fp','b','bp']:
            if i == 'r':
                rotate_r(perm)
            elif i == 'rp':
                rotate_rp(perm)
            elif i == 'l':
                rotate_l(perm)
            elif i == 'lp':
                rotate_lp(perm)
            elif i == 'u':
                rotate_u(perm)
            elif i == 'up':
                rotate_up(perm)
            elif i == 'd':
                rotate_d(perm)
            elif i == 'dp':
                rotate_dp(perm)
            elif i == 'f':
                rotate_f(perm)
            elif i == 'fp':
                rotate_fp(perm)
            elif i == 'b':
                rotate_b(perm)
            elif i == 'bp':
                rotate_bp(perm)
        

if __name__ == '__main__':
    moves=list(map(str, input("moves: ").strip().split()))
    ans=main(moves)
    print(f"\nOrder of permutation: {ans}\n")
