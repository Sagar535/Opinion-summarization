def ScalarProduct(a, X2):
    X2[1]=a*X2[1]
    return X2

def DotProduct(X1, X2):
    sum=0
`   for one in X1:
        for two in X2:
            if one[0]!=two[0]:
                sum+=0
            else:
                sum+=one[1]*two[1]
    print(sum)
    return sum    
