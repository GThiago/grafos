# Gabriel Thiago
# RA: 107774

def link(x,y,ordem,p):
    if ordem[x] > ordem[y]:
        p[y] = x
    else:
        p[x] = y
        if ordem[x] == ordem[y]:
            ordem[y] = ordem[y] + 1

def find_set(x,p):
    if x != p[x]:
        p[x] = find_set(p[x],p)
    return p[x]

def union(x, y, ordem,p):
    link(find_set(x,p), find_set(y,p), ordem,p)
