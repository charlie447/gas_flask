var lineChart = echarts.init(document.getElementById('main_line_chart'));

option = {
    title : {
        text: '未来一周气温变化',
        subtext: '纯属虚构'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:['数据1','数据2']
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            data : ['周一','周二','周三','周四','周五','周六','周日']
        }
    ],
    yAxis : [
        {
            type : 'value',
            axisLabel : {
                formatter: '{value} 单位'
            }
        }
    ],
    series : [
        {
            name:'最高气温',
            type:'line',
            data:[],
            markPoint : {
                data : [
                    {type : 'max', name: '最大值'},
                    {type : 'min', name: '最小值'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: '平均值'}
                ]
            }
        },
        {
            name:'最低气温',
            type:'line',
            data:[],
            markPoint : {
                data : [
                    {name : '周最低', value : -2, xAxis: 1, yAxis: -1.5}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name : '平均值'}
                ]
            }
        }
    ]
};

// lineChart.setOption(option);
lineChart.showLoading();

var line1 = [
    [5, 20, 36, 10, 10, 20,11],
    [2, 8, 29, 21, 20, 30,23],
    [1, 30, 36, 20, 30, 10,31],
    [5, 26, 30, 16, 12, 17,12]
]
var line2 = [
    [2, 8, 29, 21, 20, 30,23],
    [1, 30, 36, 20, 30, 10,11],
    [5, 20, 36, 10, 10, 20,24],
    [21, 20, 35, 10, 30, 10,18]
]
// option.series[0].data = line1[0];
// option.series[1].data = line2[0];
// console.log(option.series[1].data);

lineChart.setOption(option)

function fetchData(cb,index){
    // 通过 setTimeout 模拟异步加载
    setTimeout(function () {
        cb({
            
            data_line1: line1[index],
            data_line2:line2[index]

        });
    }, 3000);
}
function onAjaxTable(e){
    
    var index_data = e.getAttribute("data")
    console.log(index_data)
    var table_index = Number(index_data)

    var new_option = {
        title : {
            text: '未来一周气温变化',
            subtext: '横向对比'
        },
        tooltip : {
            trigger: 'axis'
        },
        legend: {
            data:['数据1','数据2']
        },
        toolbox: {
            show : true,
            feature : {
                mark : {show: true},
                dataView : {show: true, readOnly: false},
                magicType : {show: true, type: ['line', 'bar']},
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        calculable : true,
        xAxis : [
            {
                type : 'category',
                boundaryGap : false,
                data : ['周一','周二','周三','周四','周五','周六','周日']
            }
        ],
        yAxis : [
            {
                type : 'value',
                axisLabel : {
                    formatter: '{value} 单位'
                }
            }
        ],
        series : [
            {
                name:'最高气温',
                type:'line',
                data:line1[table_index],
                markPoint : {
                    data : [
                        {type : 'max', name: '最大值'},
                        {type : 'min', name: '最小值'}
                    ]
                },
                markLine : {
                    data : [
                        {type : 'average', name: '平均值'}
                    ]
                }
            },
            {
                name:'最低气温',
                type:'line',
                data:line2[table_index],
                markPoint : {
                    data : [
                        {name : '周最低', value : -2, xAxis: 1, yAxis: -1.5}
                    ]
                },
                markLine : {
                    data : [
                        {type : 'average', name : '平均值'}
                    ]
                }
            }
        ]
    };
    
    lineChart.setOption(new_option);
    
}

fetchData(function(data){
    lineChart.hideLoading();
    var new_option = {
        title : {
            text: '未来一周气温变化',
            subtext: '横向对比'
        },
        tooltip : {
            trigger: 'axis'
        },
        legend: {
            data:['数据1','数据2']
        },
        toolbox: {
            show : true,
            feature : {
                mark : {show: true},
                dataView : {show: true, readOnly: false},
                magicType : {show: true, type: ['line', 'bar']},
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        calculable : true,
        xAxis : [
            {
                type : 'category',
                boundaryGap : false,
                data : ['周一','周二','周三','周四','周五','周六','周日']
            }
        ],
        yAxis : [
            {
                type : 'value',
                axisLabel : {
                    formatter: '{value} 单位'
                }
            }
        ],
        series : [
            {
                name:'最高气温',
                type:'line',
                data:line1[2],
                markPoint : {
                    data : [
                        {type : 'max', name: '最大值'},
                        {type : 'min', name: '最小值'}
                    ]
                },
                markLine : {
                    data : [
                        {type : 'average', name: '平均值'}
                    ]
                }
            },
            {
                name:'最低气温',
                type:'line',
                data:line2[2],
                markPoint : {
                    data : [
                        {name : '周最低', value : -2, xAxis: 1, yAxis: -1.5}
                    ]
                },
                markLine : {
                    data : [
                        {type : 'average', name : '平均值'}
                    ]
                }
            }
        ]
    };
    lineChart.setOption(new_option);
})


