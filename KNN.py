# encoding: utf-8
import math
"""
簡易KNN sample分析, 參考：http://enginebai.logdown.com/posts/241676/knn 此篇文章出來的
"""

def create_trainset():
    """
    產生訓練樣本
    """
    trainset_data = dict()
    trainset_data['Lexus'] = (15, 25, 0, 5, 8, 3)
    trainset_data['BMW'] = (35, 40, 1, 3, 3, 2)
    trainset_data['iphone'] = (5, 0, 35, 50, 0, 0)
    trainset_data['htc'] = (1, 5, 32, 15, 0, 0)
    trainset_data['Lebron James'] = (10, 5, 7, 0, 2, 30)
    trainset_data['Jeremy Lin'] = (5, 5, 5, 15, 8, 32)
    
    """
    產生訓練樣本所屬類別
    """
    trainset_class = dict()
    trainset_class['Lexus'] = 'Car'
    trainset_class['BMW'] = 'Car'
    trainset_class['iphone'] = 'Phone'
    trainset_class['htc'] = 'Phone'
    trainset_class['Lebron James'] = 'Basketball'
    trainset_class['Jeremy Lin'] = 'Basketball'
    
    return trainset_data,trainset_class

def cosine_sim(v1,v2):
    """
    計算每兩個向量間的Cosine距離，距離越近，相似度越高
    簡易公式複習：xyz.../(x^2+y^2+z^2+...)^1/2
    """
    sum_xx = 0.0
    sum_xy = 0.0
    sum_yy = 0.0
    
    #運用math library
    for i in range(len(v1)):
        sum_xx += math.pow(v1[i],2)
        sum_yy += math.pow(v2[i],2)
        sum_xy += v1[i]*v2[i]
    return sum_xy/math.sqrt(sum_xx*sum_yy)


def KNN_algorithm(input_data,trainset_data,trainset_class,k):
    """
    KNN演算法
    1. 計算每個train data與欲計算data的距離
    2. 選定Ｋ值
    3. 接著在Ｋ個相近點投票，選定欲計算的data屬於哪個分類
    4. 印出結果
    """

    distance = dict()

    print '1. 計算每個距離:'
    for i in trainset_data:
        distance[i] = cosine_sim(trainset_data[i],input_data)
    for name in distance:
        print name,":", distance[name]
        
    print '' #空格
    print '2. 取K個最近鄰居的分類, k = ', k,':'
    class_k = dict()

    rank = sorted(distance,key = distance.get,reverse = True) #由大到小排列好

    for count in range(len(rank)):
        class_k[count] = trainset_class[rank[count]]
        print 'similarity(',rank[count],') = ',distance[rank[count]],',class:',class_k[count]
        if count+1 >= k:
            break
            
    print ''
    print '3. 決定票數和決定分類:'
    result = dict()
    ctr_phone, ctr_car, ctr_basketball = 0,0,0 #這邊應該要再修改得更漂亮，但我想不出來

    for i in range(len(class_k)):

        if 'Phone' in class_k.get(i):
            ctr_phone +=1
        result['Phone'] = ctr_phone

        if 'Car' in class_k.get(i):
            ctr_car += 1
        result['Car'] = ctr_car

        if 'Basketball' in class_k.get(i):
            ctr_basketball += 1
        result['Basketball'] = ctr_basketball
    print result
    for name in result:
        print name,":",result[name]
        
    final_result = ''
    if (k % 2 != 0):   
        for i in enumerate(sorted(result,key = result.get,reverse = True)):
            if i[0] == 0:
                final_result = i[1]
                
    print ''
    print "4. 輸入的資料分類為:",final_result



if __name__ == '__main__':
    
    input_data = (50, 55, 2, 10, 8, 5)
    trainset_data,trainset_class = create_trainset()
    KNN_algorithm(input_data,trainset_data,trainset_class,k = 3)