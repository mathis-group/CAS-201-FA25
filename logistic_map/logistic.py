import math

def logisitc(r,xt):
    xt_plus = r * xt * (1 - xt)
    return xt_plus

def run_logistic(r, x0, time_steps):
    xs = [x0]
    for k in range(time_steps + 1):
        xt_plus = logistic(r,x0)
        xs.append(xt_plus)
        x0 = xt_plus

    return xs # the value of x from x0 to x_time_steps

def run_logistic_np(r, x0, time_steps):
    
    xs = np.zeros(time_steps+1)
    xs[0] = x0
    for k in range(time_steps + 1):
        xt_plus = logistic(r,x0)
        xs.append(xt_plus)
        x0 = xt_plus

    return xs # the value of x from x0 to x_time_steps