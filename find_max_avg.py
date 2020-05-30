class Sol:
    def find_max_avg(self,arr,k):
        m,max_avg=0,0
        for i in range(len(arr)-k):
            max_avg=max((sum(arr[i:i+4])/k),m)
            m=max_avg
        return max_avg

if __name__ == '__main__':
    p=Sol()
    print(p.find_max_avg([1,12,-5,-6,50,3],4))
