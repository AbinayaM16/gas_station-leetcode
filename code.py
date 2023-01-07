def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if(sum(gas)<sum(cost)):
            return -1
        i=0
        j=0
        while(i<len(gas) and j<len(gas)):
            ans=0
            if(gas[i]>=cost[i]):
                ans=gas[i]
                length=0
                while(ans>=cost[i]):
                    ans-=cost[i]
                    if(i==len(gas)-1):
                        i=0
                    else:
                        i+=1
                    ans+=gas[i]
                    length+=1
                    if(length==len(gas)):
                        return i
            else:
                i+=1
                j+=1
        return -1
