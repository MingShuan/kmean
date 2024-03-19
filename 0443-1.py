
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#分組有4個質心所以分4組
def group(data_points,initial):
    sum_distance = 0
    #data_points每個點都對每個初始點(或更新的質心點)計算距離
    for key,items in data_points.items():
        distance_data=[]
        for index in range(4): #對4個初始點計算距離
            initial_points = initial[index]
            distance = ((key[0]-initial_points[0])**2+(key[1]-initial_points[1])**2)**0.5
            distance_data.append(distance)
        # 對距離取最小值，但我們要的不是距離而是索引值,索引值=分組號碼
        min_distance = distance_data.index(min(distance_data))
        data_points[key]=min_distance #更新每個點所在的區域
        sum_distance = sum_distance + min(distance_data)#更新總距離
    print(sum_distance/15)#列印這次的距離差


   #更新質量座標
def update(data_points,initial):
    initial_x = [0 for _ in range(4)]#初始每個x座標，y座標，數量
    initial_y = [0 for _ in range(4)]
    number=[0 for _ in range(4)]
    for key,values in data_points.items():
        index = values#區域號碼對應list的index
        number[index] =number[index]+1 #更新每個區域的數量，x的相加，y相加
        initial_x[index] = float(key[0]) + float(initial_x[index])
        initial_y[index] = float(key[1]) + float(initial_y[index])
    #更新每個質心點的位置
    for i in range(len(initial)):
        initial[i] = (initial_x[i]/number[i],initial_y[i]/number[i])


def plot(data_points,initial):
    plot_data=[[0 for j in range(10)]for i in range(10)]
    for i in range(10):
        for j in range(10):
            x=i/1
            y=j/1
            dist_data=[]
            for point in initial:
                dist=((x-point[0])**2+(y-point[1])**2)**0.5
                dist_data.append(dist)
            min_dist = dist_data.index(min(dist_data))
            plot_data[i][j]=min_dist
    ax.imshow(plot_data,cmap='viridis')
    ax.set_title('kmean')
    return[ax]


#設置data_point key是點的座標,values是分組號碼 跟質心起點
data_points = {(2,5):0, (3,2):0, (3,3):0, (3,4):0, (4,3):0, (4,4):0, (6,3):0, (6,4):0, (6,6):0, (7,2):0, (7,5):0, (7,6):0, (7,7):0, (8,6):0, (8,7):0}
# 跟質心起點座標，索引值對應分組號碼
initial = [(2,2), (4,6), (6,5), (8,8)]
def update_plot(frame):
    group(data_points, initial)
    ax.clear()
    plot(data_points, initial)
    if frame==10:
        anime.event_source.stop()
    update(data_points, initial)
    # print(initial)

fig,ax=plt.subplots()
anime=animation.FuncAnimation(fig,update_plot,frames=range(100),interval=50)
plt.show()