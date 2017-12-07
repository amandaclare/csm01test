import matplotlib.pyplot as plt

def gen_linear(m, c):
    x_vals = range(0,10)
    y_vals = [ m*x + c for x in x_vals]
    return (x_vals, y_vals)


def gen_poly(a, n):
    x_vals = range(0,10)
    y_vals = [ a * (x**n) for x in x_vals]
    return (x_vals, y_vals)

def plot_both():
    (x, y) = gen_linear(5, 3)
    plt.plot(x, y, 'b-')
    plt.plot(x, y, 'bv')
    
    (x, y) = gen_poly(5, 3)
    plt.plot(x, y, 'r-')
    plt.plot(x, y, 'rv')

    plt.savefig("linpoly.png")
    plt.show()

def plot_loglog():
    (x, y) = gen_poly(5, 3)
    plt.loglog(x, y, 'r-')
    plt.loglog(x, y, 'rv')
    plt.savefig("loglog.png")
    plt.show()

if __name__ == "__main__":
    plot_loglog()
