import statistics
import random
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv('medium_data.csv')

data = df['reading_time'].tolist()

def find_mean_of_rand_data():
    dataset = []
    for i in range(0,100):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


def show_graph(data):
    mean = statistics.mean(data)
    fig = ff.create_distplot([data], ['Mean'], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0,12], mode='lines', name='Mean'))
    fig.show()

def setUp():
    mean_list = []
    for i in range(0,1000):
        means_set = find_mean_of_rand_data()
        mean_list.append(means_set)
    mean_of_sd = statistics.mean(mean_list)
    stdev_of_sd = statistics.stdev(mean_list)
    mean_of_data = statistics.mean(data)
    stdev_of_data = statistics.stdev(data)
    show_graph(mean_list)
    print('Mean of sampling distribution: \t', mean_of_data)
    print('Stdev of sampling distribution: \t', stdev_of_data)
    print('Mean of sampling distribution: \t', mean_of_sd)
    print('Stdev of sampling distribution: \t', stdev_of_sd)

setUp()