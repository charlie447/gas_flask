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
            data : ['201301','201302','201303','201304','201305','201306','201307','201308','201309','201310','201311','201312','201401','201402','201403','201404','201405','201406','201407','201408','201409','201410','201411','201412','201501','201502','201503','201504','201505','201506','201507','201508','201509','201510','201511','201512','201601','201602','201603','201604','201605','201606','201607','201608','201609','201610','201611','201612','201701','201702','201703','201704','201705']
        }
    ],
    yAxis : [
        {
            type : 'value',
            axisLabel : {
                formatter: '{value} 个'
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
    [20000,13954,20706,19197,21502,21491,20162,19074,22504,25839,27188,31288,24910,19604,24682,21777,22737,19280,21302,22740,21055,22168,24910,31699,29425,20197,26150,22767,21031,18898,20181,19925,19548,20709,24885,29182,33880,22414,26278,20707,20708,20197,20132,18707,21491,22722,30483,29472,26272,23748,26216,21418,19333, , ],
    [2387,1513,2027,2069,2251,2137,2131,2193,2333,2883,2443,2587,2086,1342,1831,1907,1853,1634,1617,1790,1627,1800,2119,2719,2854,2222,2915,2087,1832,1501,1915,1833,1734,1713,2092,2322,2694,2343,2399,1815,1819,1788,1567,1644,1743,1865,2827,2722,2274,2058,1899,1524,1406, null, null],
    [1121,694,1058,918,719,840,827,920,993,1241,1160,1657,1468,1067,1173,952,1079,915,1081,1390,1084,1204,1506,1785,1763,1033,1414,1385,1287,1208,1200,1195,1501,1461,1877,1887,2791,1465,2283,1568,1317,1523,1320,1051,1672,1528,1980,1569,1706,1642,1755,1336,1471, null, null],
    [20000,13954,20706,19197,21502,21491,20162,19074,22504,25839,27188,31288,24910,19604,24682,21777,22737,19280,21302,22740,21055,22168,24910,31699,29425,20197,26150,22767,21031,18898,20181,19925,19548,20709,24885,29182,33880,22414,26278,20707,20708,20197,20132,18707,21491,22722,30483,29472,26272,23748,26216,21418,19333, null, null]
]
var line2 = [
    [ null, null, null, null, null, null, null, null, null, null, null, null,25496.27,19842.58,23701.01,21754.41,21018.52,20491.54,20683.29,21447.45,21544.89,21544.45,26190.29,29998.37,28219.49,22363.95,26117.98,24881.95,22925.05,19282.83,20465.17,22936.18,19893.62,20745.53,24412.68,30195.48,null, null, null, null, null, null, null, null, null, null, null, null,33275.93,25637.67,27706.93,23674,21005.54, null, null],
    [null, null, null, null, null, null, null, null, null, null, null, null,2131.49,1620.25,1659.99,1710.8,1910.09,1821.91,1825.1,1927.79,1704.76,1886.73,2268.81,2749.89,2720.92,2446.75,2453.15,2283.47,1856.41,1646.48,1843.48,1878.42,1588.49,1640.03,1891.48,2210.5,null, null, null, null, null, null, null, null, null, null, null, null,2968.63,2689.19,2179.54,1845.04,1700.01, null, null],
    [null, null, null, null, null, null, null, null, null, null, null, null,1325.92,1137.68,1177.72,1134.83,1073.26,1043.54,964.8,1269.54,1209.24,1383.96,1558.61,1733.25,1725.85,1228.33,1269.7,1388.72,1256.45,1241.08,1172.21,1490.76,1353.92,1455.32,1896.65,1892.77,null, null, null, null, null, null, null, null, null, null, null, null,2282.95,2184.41,2087.75,1797.64,1527.54, null, null],
    [20000,6475.03,23911.94,18052.84,23511.76,22058.35,19137.34,17726.9,25451.87,30003.38,30033.26,36610.1,5946.59,15596.06,18677.46,16757.4,17249.89,11709.58,19265.47,22963.14,14973.89,15298.74,20577.95,29378.74,34338.43,18936.59,27092.72,23149.73,18985.38,19561.72,18967.28,16938.41,19599.66,20740.1,25975.03,26913.15,38635.47,23947.69,25738.11,18603.73,21495.2,21796.8,20095.99,18091.89,24017.17,24468.15,35374.68,28410.18,35453.3,23540.06,26996.77,21001.71,21338.7,21141.55,20815.69,19164.47,22560.16,23804.71,32259.45,30221.29]
]
// option.series[0].data = line1[0];
// option.series[1].data = line2[0];
// console.log(option.series[1].data);

lineChart.setOption(option)

function fetchData(cb,index){
    // 通过 setTimeout 模拟异步加载
    setTimeout(function () {
        cb({
            
            data_line1:line1[index],
            data_line2:line2[index]

        });
    }, 3000);
}
function onAjaxTable(e){
    
    var index_data = e.getAttribute("data")
    console.log(index_data)
    var table_index = Number(index_data)
    text_list = ["LSTM-全市","LSTM-徐汇","LSTM-宝山","SARIMA-全市"];
    // console.log(text_list[table_index]);

    var new_option = {
        title : {
            text: text_list[table_index],
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
                data : ['201301','201302','201303','201304','201305','201306','201307','201308','201309','201310','201311','201312','201401','201402','201403','201404','201405','201406','201407','201408','201409','201410','201411','201412','201501','201502','201503','201504','201505','201506','201507','201508','201509','201510','201511','201512','201601','201602','201603','201604','201605','201606','201607','201608','201609','201610','201611','201612','201701','201702','201703','201704','201705','201706','201707']
            }
        ],
        yAxis : [
            {
                type : 'value',
                axisLabel : {
                    formatter: '{value} 个'
                }
            }
        ],
        series : [
            {
                name:'原始值',
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
                name:'拟合值',
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
            text: 'LSTM-宝山',
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
                data : ['201301','201302','201303','201304','201305','201306','201307','201308','201309','201310','201311','201312','201401','201402','201403','201404','201405','201406','201407','201408','201409','201410','201411','201412','201501','201502','201503','201504','201505','201506','201507','201508','201509','201510','201511','201512','201601','201602','201603','201604','201605','201606','201607','201608','201609','201610','201611','201612','201701','201702','201703','201704','201705','201706','201707']
            }
        ],
        yAxis : [
            {
                type : 'value',
                axisLabel : {
                    formatter: '{value} 个'
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


