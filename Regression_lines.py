#Gaurav More
#PRN: 10303320181124510065 [DA]

x_score = [15 , 12 , 8  , 8 ,  7 ,  7 ,  7 ,  6   , 5  , 3]
y_score = [10  ,25 , 17  ,11 , 13 , 17 , 20 , 13 , 9  , 15]
n=10

x_sum =0
y_sum =0
product = 0
sq=0

for i in range (0,n):
    x_sum+=x_score[i]
    y_sum+=y_score[i]
    product += x_score[i]*y_score[i]
    sq += x_score[i]*x_score[i]

x_mean = float((x_sum)/n)
y_mean = float((y_sum)/n)

slope = (n*product - x_sum*y_sum)/(n*sq - x_sum*x_sum)
constant = y_mean - (x_mean*slope)
ans = slope*10+constant
print('%.1f'%ans)
