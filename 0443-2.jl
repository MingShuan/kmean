using Plots
#分組有4個質心所以分4組
function group(data_points, initial)
    sum_distance = 0
    #data_points每個點都對每個初始點(或更新的質心點)計算距離
    for key in keys(data_points)
        distance_data = []
        for index in 1:4#對4個初始點計算距離
            initial_points = initial[index]
            distance = sqrt((key[1] - initial_points[1])^2 + (key[2] - initial_points[2])^2)
            push!(distance_data, distance)
        end
        # 對距離取最小值，但我們要的不是距離而是索引值,索引值=分組號碼
        min_distance = argmin(distance_data)
        data_points[key] = min_distance#更新每個點所在的區域
        sum_distance += minimum(distance_data)#更新總距離
    end
    println(sum_distance / 15)
end
#更新質量座標
function update(data_points,initial)
    num =[0,0,0,0]#初始每個x座標，y座標，數量
    x=zeros(Float64,4)
    y=zeros(Float64,4)
    for (key, values) in data_points
        num[values]=num[values]+1#更新每個區域的數量，x的相加，y相加
        x[values]=x[values]+key[1]
        y[values]=y[values]+key[2]
    end
    #更新每個質心點的位置
    for i in 1:4
        initial[i]=(x[i]/num[i],y[i]/num[i])
    end

end
function plot(initial)
    plot_data=zeros(Float64,10,10)
    for i in 1:10
        for j in 1:10
            distance_data=[]
            for item in initial
                distance = sqrt((i-item[1])^2+(j-item[2])^2)
                push!(distance_data,distance)
            min_distance = argmin(distance_data)
            plot_data[i,j]=min_distance
            end
        end
    end
    heatmap(plot_data, aspect_ratio=1, color=:viridis, title="k-mean")

end

data_points=Dict((2,5)=>0, (3,2)=>0, (3,3)=>0, (3,4)=>0, (4,3)=>0, (4,4)=>0, (6,3)=>0, (6,4)=>0, (6,6)=>0, (7,2)=>0, (7,5)=>0, (7,6)=>0, (7,7)=>0, (8,6)=>0, (8,7)=>0)
initial = [(2.0,2.0), (4.0,6.0), (6.0,5.0), (8.0,8.0)]

anim=@animate for i in 1:10
    group(data_points,initial)
    plot(initial)
    update(data_points,initial)
end
gif(anim,"k-mean.gif",fps=1)
