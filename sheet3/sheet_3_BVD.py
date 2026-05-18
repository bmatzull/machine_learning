import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def native_f(x):
    return  ((.8*x-0.2)-0.5)**2 + 0.6*np.sin(x*5) + -0.3*x

# you dont need to modify this class
class PolyModel:
    """class to create and fit polynomial models"""
    def __init__(self, deg = 2) -> None:
        self.deg= deg

    def fit(self, X, y):
        self.coef = np.polyfit(X, y, deg=self.deg)
        return self

    def predict(self, X):

        x = np.ones_like(X)
        y = np.zeros_like(X)
        #print(self.coef)
        for i in range(len(self.coef)):
            y += x * self.coef[-i-1]
            x=x*X
        return y


def sample_D(n = 30, interval=(0,3), var = 1):
    """ Generate a random data set D. With a uniform
    distributed x coord,
    and with a normal distributetd eps with sigma=var^2
    Parameters:
        n (int): number of generated points
        interval (list): interval on x-axis
        var (float):  error var in y = f(x) + eps
    Returns:
        list, list: x and y coordinates

    """
    # Task 1.1
    # correct next two expressions
    xx = np.random.uniform(interval[0],interval[1],n)
    noise = np.random.normal(0, np.sqrt(var), n)

    yy = native_f(xx) + noise
    return xx, yy

def induce_models(m, deg=2, n = 30, interval=(0,3), var = 1):
    """Creates a list of models using random samples
    Parameters:
        m (int): number of generated models
        deg: degree of the polynomial
    Returns:
        list: m models
    """
    models = []
    # Task 1.2
    for _ in range(m):
        x,y = sample_D(n, interval, var)
        model = PolyModel(deg=deg)
        model.fit(x,y)
        models.append(model)

    return models


def predict_all(x, models):
    """Creates predictions for all x-coordinates and all models in the models list
    Parameters:
        x (array): 1-D array with x-coordantes
        models (list): models to apply
    Returns:
        array: n x m array. m = len(x), n=len(models)

    """
     # Task 1.3
    res = np.zeros((len(models), len(x)))
    for i, model in enumerate(models):
        res[i, :] = model.predict(x)
    return res

if __name__ == '__main__':

    #demo
    x_lims = (0,3)

    xx = np.linspace(x_lims[0], x_lims[1],100)
    y_true = native_f(xx)

    #plot
    fig, ax = plt.subplots()
    ax.plot(xx, y_true, c="blue", lw=4, label="f(x)")
    model2 = PolyModel(deg=2)
    model2.fit(xx, y_true)
    ax.plot(xx, model2.predict(xx), lw=3, ls="--", label="Polynomial deg 2")

    plt.legend()
    plt.tight_layout()
    plt.show()
    #demo end


    # Task 1.4, 1.5, 1.6
    xx = np.linspace(1,2,50)
    degrees = np.arange(1,12)
    biases = []
    vars = []

    for deg in degrees:
        models = induce_models(m=100, deg=deg, n=30, interval=(0,3), var=1)
        preds = predict_all(xx, models)
        mean_preds = np.mean(preds, axis=0)

        bias2_per_x = (mean_preds - y_true) ** 2
        var_per_x = np.mean((preds - mean_preds) ** 2, axis=0)

        biases.append(np.mean(bias2_per_x))
        vars.append(np.mean(var_per_x))


    #plot Bias and Variance
    #if you solve the properly, you dont need to change anything here
    if (len(biases) == len(degrees)):
        fig, ax = plt.subplots()
        ax.plot(degrees, biases, lw = 4, c="b", label="$Bias^2$")
        print(biases)
        ax.set_xlabel("Degree")
        ax.set_ylabel("Error")
        ax2 = ax.twinx()
        ax2.plot(degrees, vars, lw = 4, c="red", label="$Var$")
        fig.legend()
        plt.show()