import matplotlib.pyplot as plt
n = int(input("Enter Number Of Process:"))
bt=[]
ct=[]
wt =[]
for i in range(n):
    print("Enter Burst Time of Process ",i+1,end=' ')
    bt.append(int(input()))
ct.append(bt[0])
for i in range(1,n):
    ct.append(bt[i]+ct[i-1])
tat=ct
for i in range(n):
    wt.append(tat[i]-bt[i])
plot=[]
for i in range(len(bt)):
    plot.append([x for x in range(bt[i]+1)])
for i in range(1,len(bt)):
    plot[i]=[x+plot[i-1][-1]-1 for x in range(1,bt[i]+1)]
for i in plot:
    plt.hist(i,1,label='Process'+str(plot.index(i)))
print("Average Turn Around Time :",sum(tat)/len(tat))
print("Average Turn Waiting Time :",sum(wt)/len(wt))
plt.title("FCFS-Gantt Chart")
plt.legend()
plt.ylim(0,1)
plt.show()
