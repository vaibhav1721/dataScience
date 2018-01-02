import scipy
from pandas import read_csv
import scipy.stats

def compute_avg():
    baseball_data = read_csv("baseball_data.csv")
    baseball_data_left = baseball_data[baseball_data['handedness']=='L']
    baseball_data_right = baseball_data[baseball_data['handedness']=='R']

    result = scipy.stats.ttest_ind(baseball_data_left['avg'],baseball_data_right['avg'],equal_var=False)

    if result[1] <= .05:
        return (False, result)
    else:
        return (True, result)

if __name__ == '__main__':
    result = compute_avg()
    print result
    baseball_data = read_csv("baseball_data.csv")
    print baseball_data