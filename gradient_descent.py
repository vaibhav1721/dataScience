import numpy
from pandas import read_csv, Series


def normalize_features(array):
    """
    normalize the features array containing height and weight
    :param array:
    :return:
    """

    array_normalized = (array - array.mean())/array.std()
    mu = array.mean()
    sigma = array.std()

    return array_normalized,mu,sigma


def compute_cost(features,values,theta):
    """"
    computing the cost function... takes features(height,weight) and values(HR) and theta as weight of indivuals features
    """
    m = len(values)
    sum_of_square_error = numpy.square(numpy.dot(features,theta)-values).sum()
    cost = sum_of_square_error/(2*m)
    return cost


def gradient_descent(features,theta,values,alpha,num_iteration):
    """

    :param features: height, weight
    :param theta: cost of individuals features
    :param values: Heightest Run
    :param alpha: the learning rate
    :param num_iteration: number of iterations
    :return: theta , series containing cost_history
    """
    cost_history = []
    m = len(values)
    for i in range(num_iteration):
        predicted_value = numpy.dot(features,theta)
        theta = theta - alpha / m * numpy.dot((predicted_value-values),features)
        cost = compute_cost(features,values,theta)
        cost_history.append(cost)

    return theta,Series(cost_history)


if __name__== '__main__':
    baseball_data = read_csv("baseball_data.csv")

    features = baseball_data['height']['weight']
    values = baseball_data['HR']

    m = len(values)
    theta = ('2,3')
    alpha = 2
    num_itr = 1157

    features,mu,sigma = normalize_features(features,theta)
    print baseball_data
    #print(gradient_descent(features,theta,values,alpha,num_itr))