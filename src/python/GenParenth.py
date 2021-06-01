def genParenthesis(openB,closeB,n,s=[]):
    #base case
    if(closeB==n):
        print(''.join(s))
        return
    else:
        if(openB>closeB):
            s.append(')')
            genParenthesis(openB,closeB+1,n,s)
            s.pop()
        if(openB<n):
            s.append('(')
            genParenthesis(openB+1,closeB,n,s)
            return


genParenthesis(0,0,2)        
