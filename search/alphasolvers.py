import numpy as np
import cvxopt
import cvxopt.solvers

def Alpha_Calculator(Kernel, no_sample, y, C_value):
    ###not done by me
    #for solving Quadratic Programming
    P = cvxopt.matrix(np.outer(y,y) * Kernel) #y*y ko matrix
    q = cvxopt.matrix(np.ones(no_sample) * -1)
    

    A = cvxopt.matrix(y, (1, no_sample), 'd')

    b = cvxopt.matrix(0.0)
    print('alphasolver mathi ko success')
    if C_value is None:
         G = cvxopt.matrix(np.diag(np.ones(no_sample) * -1))
         h = cvxopt.matrix(np.zeros(no_sample))
    else:
        tmp1 = np.diag(np.ones(no_sample) * -1)
        tmp2 = np.identity(no_sample)
        G = cvxopt.matrix(np.vstack((tmp1, tmp2)))
        tmp1 = np.zeros(no_sample)
        tmp2 = np.ones(no_sample) * C_value
        h = cvxopt.matrix(np.hstack((tmp1, tmp2)))
        
    solution = cvxopt.solvers.qp(P, q, G, h, A, b)
    # solve QP problem

    a = np.ravel(solution['x'])

    return a
    
    # Lagrange multipliers a1, a2, a3, a4....

     ###not done by me
