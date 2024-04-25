import time
def code_timer(precision=30):
    average={}
    for i in range(precision):
        times={}
        start=time.time()

        ##code##
        pass
        ########

        end=time.time()
        times['placeholder_1']=end-start

        ###########comparison###########

        start=time.time()

        ##code##
        pass
        ########
        
        end=time.time()
        times['placeholder_2']=end-start

        #result
        for key, value in times.items():
            if value==min(times.values()):
                if key in average:
                    average[key]+=1
                else:
                    average[key]=1
    for key, value in average.items():
        if value==max(average.values()):
            print(f'On average, {key} was faster\nWon the race {value} out of {precision} times')
            return key

code_timer()