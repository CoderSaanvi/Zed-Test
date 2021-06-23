import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics as s
import random
df=pd.read_csv('school1.csv')
data=df["Math_score"].tolist()
populationMean=s.mean(data)
populationSd=s.stdev(data)
def extract(counter): 
    dataSet=[]
    for i in range(0,counter): 
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    sampleMean=s.mean(dataSet)
    return sampleMean
meanList=[]
for i in range(0,1000): 
    setOfMeans=extract(100)
    meanList.append(setOfMeans)
sd=s.stdev(meanList)
mean=s.mean(meanList)
firstsdStart,firstsdEnd=mean-sd,mean+sd
secondsdStart,secondsdEnd=mean-(2*sd),mean+(2*sd)
thirdsdStart,thirdsdEnd=mean-(3*sd),mean+(3*sd)
#fig=ff.create_distplot([meanList],["Math_score"],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="Mean"))
#fig.show()
print("Mean: ",mean)
print("Standard Deviation: ",sd)
df=pd.read_csv('school2.csv')
data=df["Math_score"].tolist()
meanOfMath2=s.mean(data)
print("Mean of Math 2: ",meanOfMath2)
df=pd.read_csv('school3.csv')
data=df["Math_score"].tolist()
meanOfMath3=s.mean(data)
print("Mean of Math 3: ",meanOfMath3)
df=pd.read_csv('school4.csv')
data=df["Math_score"].tolist()
meanOfMath4=s.mean(data)
print("Mean of Math 4: ",meanOfMath4)
fig=ff.create_distplot([meanList],["Math_score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[meanOfMath2,meanOfMath2],y=[0,0.20],mode="lines",name="Mean 2"))
fig.add_trace(go.Scatter(x=[meanOfMath3,meanOfMath3],y=[0,0.20],mode="lines",name="Mean 3"))
fig.add_trace(go.Scatter(x=[meanOfMath4,meanOfMath4],y=[0,0.20],mode="lines",name="Mean 4"))
fig.show()
zedScore1=(mean-meanOfMath2)/sd
zedScore2=(mean-meanOfMath3)/sd
zedScore3=(mean-meanOfMath4)/sd
print("Zed Score 1: ",zedScore1)
print("Zed Score 2: ",zedScore2)
print("Zed Score 3: ",zedScore3)