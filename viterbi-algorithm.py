""" Author: Varun Kumar Reddy B
    Viterbi Algorithm
     """

obsNames={0:"HOT",1:"COLD"}
def Decode(observation,A,B,phi):
    observations=len(observation)
    states=len(phi)
    v=[[0 for x in range(observations+1)]for y in range(states)]
    b=[[0 for x in range(observations+1)]for y in range(states)]
    for s in range(states):
        v[s][0]=phi[s]*B[s][observation[0]-1]
        b[s][0]=0
    for t in range(1,observations):
        for i in range(states):
            tmp=[(v[j][t-1]*A[j][i]*B[i][observation[t]-1],j) for j in range(states)]
            v[i][t],b[i][t]=max(tmp)
    result=max((v[s][observations-1],s) for s in range(states))
    backPointer=result[1]
    result=[]
    for t in range(observations-1,-1,-1):
        result.insert(0,obsNames[backPointer])
        backPointer=b[backPointer][t]
    return result

observation=[[3,3,1,1,2,2,3,1,3],[3,3,1,1,2,3,3,1,2]]
A=[[0.7,0.3],[0.4,0.6]]
phi=[0.8,0.2]
B=[[0.2,0.4,0.4],[0.5,0.4,0.1]]
o1="".join([str(x) for x in observation[0]])
o2="".join([str(x) for x in observation[1]])
print "Sequence of States for "+o1+" are :"+str(Decode(observation[0],A,B,phi))
print "Sequence of States for "+o2+" are :"+str(Decode(observation[1],A,B,phi))
