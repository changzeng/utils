# encoding: utf-8

import plotly
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs

plotly.offline.init_notebook_mode()

def get_div(a, b):
    if b == 0:
        return 0
    return float(a)/float(b)

# 绘制多条直线
def plot_line(x_list, y_list, x_name="", y_name="", title="", name_list=None):
    plot_data = []
    for i in range(len(x_list)):
        if name_list != None:
            trace = Scatter(name=name_list[i], x=x_list[i], y=y_list[i])
        else:
            trace = Scatter(x=x_list[i], y=y_list[i])
        plot_data.append(trace)
    fig = Figure(data=plot_data, layout=Layout(title=title, xaxis=dict(title=x_name), yaxis=dict(title=y_name)))
    plotly.offline.iplot(fig)

# 绘制单条柱状图
def plot_bar(x, y, title=""):
    plot_multi_bar([x], [y], title=title)

# 绘制多条柱状图
def plot_multi_bar(x_list, y_list, x_name="", y_name="", title="", name_list=None):
    plot_data = []
    for i in range(len(x_list)):
        if name_list != None:
            trace = Bar(name=name_list[i], x=x_list[i], y=y_list[i])
        else:
            trace = Bar(x=x_list[i], y=y_list[i])
        plot_data.append(trace)
    fig = Figure(data=plot_data, layout=Layout(title=title, xaxis=dict(title=x_name), \
            yaxis=dict(title=y_name)))
    plotly.offline.iplot(fig)

# 绘制单条直线
def plot_single_line(x, y, x_name="", y_name="", title=""):
    plot_line([x], [y], x_name, y_name, title)

# 绘制多条直线
def plot_multi_line(x_list, y_list, x_name="", y_name="", title="", name_list=None):
    plot_line(x_list, y_list, x_name, y_name, title, name_list)

# 分布以及分布占比
def plot_dist_and_proportion(x, dist, prop, x_name="", y_name="", title=""):
    accu = []
    _accu = 0
    _prop = []
    _sum = sum(prop)
    for item in prop:
        _accu += item
        _prop.append(get_div(item, _sum))
        accu.append(get_div(_accu, _sum))
    _dist = Scatter(x=x,y=dist, name="分布")
    _prop = Bar(x=x, y=_prop, name="占比", yaxis='y2')
    _accu = Scatter(x=x, y=accu, name="累积占比", yaxis='y2')
    data = [_dist, _prop, _accu]

    layout = Layout(
        title=title,
        xaxis=dict(
            title=x_name
        ),
        yaxis=dict(
            title=y_name
        ),
        yaxis2=dict(
            title="占比",
            titlefont=dict(
                color='rgb(148, 103, 189)'
            ),
            tickfont=dict(
                color='rgb(148, 103, 189)'
            ),
            overlaying='y',
            side='right'
        )
    )
    fig = Figure(data=data, layout=layout)
    plotly.offline.iplot(fig)

# 绘制两条坐标轴不一致的直线
def plot_two_axis(x, y1, y2, x_name="", axis_name_list=["", ""], name_list=["", ""], title=""):
    a = Bar(x=x, y=y1, name=name_list[0])
    b = Scatter(x=x, y=y2, name=name_list[1], yaxis='y2')
    data = [a, b]

    layout = Layout(
        title=title,
        xaxis=dict(
            title=x_name
        ),
        yaxis=dict(
            title=axis_name_list[0]
        ),
        yaxis2=dict(
            title=axis_name_list[1],
            titlefont=dict(
                color='rgb(148, 103, 189)'
            ),
            tickfont=dict(
                color='rgb(148, 103, 189)'
            ),
            overlaying='y',
            side='right'
        )
    )
    fig = Figure(data=data, layout=layout)
    plotly.offline.iplot(fig)

# 绘制散点
def plot_scatter(x, y, x_name="", y_name="", title=""):
    plot_data = []
    trace = Scatter(x=x, y=y, mode="markers")
    plot_data.append(trace)
    fig = Figure(data=plot_data, layout=Layout(title=title, xaxis=dict(title=x_name), yaxis=dict(title=y_name)))
    plotly.offline.iplot(fig)
    
# 绘制3d数据点
def plot_3d_scatter(scatters_list, color=None, name=None):
    data = []
    layout = Layout(
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
        )
    )
    for i, scatters in enumerate(scatters_list):
        if color is None:
            _color = 'rgb(204, 204, 204)'
        else:
            _color = color[i]
        if name is None:
            _name = ""
        else:
            _name = name[i]
        x, y, z = zip(*scatters)
        trace = Scatter3d(
            name=_name,
            x=x,
            y=y,
            z=z,
            mode='markers',
            marker=dict(
                color=_color,
                size=5,
                symbol='circle',
                line=dict(
                    color='rgb(204, 204, 204)',
                    width=1
                ),
                opacity=0
            )
        )
        data.append(trace)
    fig = Figure(data=data, layout=layout)
    plotly.offline.iplot(fig)