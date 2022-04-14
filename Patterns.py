Pattern = []
#Fucntions
def Populalat():
    k = 1
    term = input(f'Input the {k}th term')
    while term != '':
        term = int(term)
        Pattern.append(term)
        k += 1
        term = input(f'Input the {k}th term')
    print(Pattern)

def find_pattern_type(Pattern,Match_A = 0,Match_G = 0,Match_F = 0,Match_Q = 0):
    for N in range(len(Pattern)-2):
        if ((Pattern[N+1])-(Pattern[N])) == ((Pattern[N+2])-(Pattern[N+1])):
            Match_A += 1
            #print(str(((Pattern[N+1])-(Pattern[N]))))
    for T in range(len(Pattern)-2):
        if ((Pattern[T+1])/(Pattern[T])) == ((Pattern[T+2])/(Pattern[T+1])):
            Match_G += 1
    for F in range(len(Pattern)-2):
        if (Pattern[F] + Pattern[F+1] )==  Pattern[F+2]:
            Match_F += 1
    for Q in range(len(Pattern)-4):
        if ((Pattern[Q+1]- Pattern[Q] ) - (Pattern[Q+2]- Pattern[Q+1] ) ) == ((Pattern[Q+3]- Pattern[Q+2] ) - (Pattern[Q+4]- Pattern[Q+3] ) ) :
            Match_Q += 1
            
    if Match_G == (len(Pattern)-2):
        return 'Geometric'
    elif Match_A == (len(Pattern)-2):
        return 'Aritmatic'
    elif Match_F == (len(Pattern)-2):
        return 'Fibonacci'
    elif Match_Q == (len(Pattern)-4):
        return 'Qadratic'
            

def Aritmatic(Pattern):
    AN  = f'{Pattern[0]} +(N-1) * {(Pattern[1])-(Pattern[0])}'
    print(AN)
    
def Geomertric(Pattern):
    AN  = f'{Pattern[0]} * {(Pattern[1])/(Pattern[0])}^(n-1)'
    print(AN)
     
#Implementation     
Populalat()
Pattern_type = find_pattern_type(Pattern)
if Pattern_type == 'Aritmatic':
    print(f'This is a {Pattern_type} pattern')
    Aritmatic(Pattern)
elif Pattern_type == 'Geometric':
    print(f'This is a {Pattern_type} pattern')
    Geomertric(Pattern)
elif Pattern_type == 'Fibonacci':
    print(f'This is a {Pattern_type} pattern')
elif Pattern_type == 'Qadratic':
    print(f'This is a {Pattern_type} pattern')
    