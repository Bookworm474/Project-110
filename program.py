import pandas as pd
import statistics as st
import random
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = st.mean(data)
mean_of_samples = []

for x in range(0,100):
    temp = []
    for x in range(0,30):
        temp.append(data[random.randint(0, (len(data)-1))])
    mean_of_samples.append(st.mean(temp))

fig = ff.create_distplot([mean_of_samples], ["Mean Reading Time"], show_hist=False)
fig.show()

print(population_mean)
print(st.mean(mean_of_samples))