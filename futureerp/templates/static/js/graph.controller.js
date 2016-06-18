
// graph main
var pie_chart_config = {
        type: 'pie',
        data: {
            datasets: [
            {
                data: [
                    150,
                    200,
                    120,
                    210,
                    70,
                ],
                backgroundColor: [
                    "#F7464A",
                    "#46BFBD",
                    "#FDB45C",
                    "#949FB1",
                    "#4D5360",
                ],
            }],
            labels: [
                "Red",
                "Green",
                "Yellow",
                "Grey",
                "Dark Grey"
            ]
        },
        options: {
            responsive: true,
	 tooltips: {
                    mode: 'label',
           	    backgroundColor: "rgb(204, 204, 0)"
                },
        },
    };

 var line_chart_config = {
            type: 'line',
            data: {
                labels: ["January", "February", "March", "April", "May", "June", "July"],

                // we can add multiple datasets here
                datasets: [{
                    label: "Year's Data",
		    backgroundColor: "rgb(0, 51, 153)",	
		    borderColor:"rgb(255, 153, 0)",	
                    data: [100, 120, 90, 180, 144, 156, 110],
                    fill: false,
                    borderDash: [5, 5],
                }]
            },

            options: {
                responsive: true,
                title:{
                    display:true,
                    text:'Weavebytes Line Chart Demo'
                },

                tooltips: {
                    mode: 'label',
           	    backgroundColor: "rgb(204, 204, 0)",
		    callbacks: { 
			title: function(tooltipItems, data) {
				var labels = data.labels;
				var labelCount = labels ? labels.length : 0;

				if (tooltipItems.length > 0) {
					var item = tooltipItems[0];

					if (item.xLabel) {
						 return "Day of Created Date :    " +  item.xLabel;
					} else if (labelCount > 0 && item.index < labelCount) {
						return labels[item.index];
					}
				}

			},			
			label: function(tooltipItem, data) {
				var datasetLabel = data.datasets[tooltipItem.datasetIndex].label || '';
				return datasetLabel + '                 :    ' + tooltipItem.yLabel;
			},
		   }
                },
                hover: {
                    mode: 'dataset'
                },
                scales: {
                    xAxes: [{
			scaleLabel: {
        		        display: true,
			        labelString: 'Day of Created Date [2016]'
      			}
		    }],
                    yAxes: [{
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: 'Values'
                        },
                        ticks: {
                            suggestedMin: 10,
                            suggestedMax: 250,
                        }
                    }]
                }
            }
        };

// Carriers graph data
  var CarrierData = {
            labels: [],
            datasets: [{
                label: 'Total Items',               
                backgroundColor: "rgb(0, 51, 153)",
                data: [],
            }]
        };

//draw the bar graph
function draw_bar_graph(){
    
	 var ctx = document.getElementById("carrier").getContext("2d");
            window.myHorizontalBar = new Chart(ctx, {                  
                type: 'horizontalBar',               
 		data: CarrierData,
                options: {
                    // Elements options apply to all of the options unless overridden in a dataset
                    // In this case, we are setting the border of each horizontal bar to be 2px wide 
                    elements: {
                        rectangle: {
                            borderWidth: 1,
			    borderColor: 'rgb(0, 51, 153)',
			    borderSkipped: 'left'
                        }
                    },

                    responsive: true,
                    legend: {
                        position: 'right',
                    },
                    title: {
                        display: true,
                        text: 'Carriers'
                    },
                  scales: {
            		xAxes: [{
                     		ticks: {
                    			beginAtZero:true,
	             		},
			scaleLabel: {
        		        display: true,
			        labelString: 'Total Items'
      			}
            		}],
 			yAxes: [{
				barPercentage: 0.6
			}],
        	    }
                }
            });
       }

// line chart data
    var lineChartData = {
        labels: ["Jun1", "Jun2", "Jun3", "Jun4", "Jun5", "Jun6", "Jun7", "Jun8", "Jun9", "Jun10"],
        datasets: [{
            label: "Price ",
            tension:0, 
            fill:false,		
            borderColor:"rgb(0, 51, 153)",
	    data: [],
            yAxisID: "y-axis-1",
        }, {
            label: "Total Items ",
            tension:0,
            fill:false,
            borderColor:"rgb(255, 153, 0)",
            data: [],
            yAxisID: "y-axis-2"
        }]
    };

function setGraphData(){
	
	//adding data for carrier data
	//addCarrierData();
	
	//adding data for line chart data
	addLineChartData();
}

//add data to for the line chart 
function addCarrierData(){

 	var carrierNames = ["Courrier Please", "Direct Courrier"];
	var total_items = [4, 10];

	var  carrier_names = CarrierData.labels;

	for(var name = 0; name < carrierNames.length; ++name){
		carrier_names[name] = carrierNames[name];	
	}
	var  carrrier_total_items = CarrierData.datasets[0].data;

	for(var index = 0; index < CarrierData.labels.length; ++index){
		carrrier_total_items[index] = total_items[index]; 	
	}
}

//add data to for the line chart 
function addLineChartData(){
 	var price = [10, 20, 35, 25, 40, 85, 35, 15, 10, 35];
	var total_items = [15, 10, 20, 15, 75, 15, 10, 20, 15, 30];

	var LineChartDataPrice = lineChartData.datasets[0].data;
	var LineChartDataTotalItems = lineChartData.datasets[1].data;

	for(var index = 0; index < lineChartData.labels.length; ++index){
		LineChartDataPrice[index] = price[index]; 	
		LineChartDataTotalItems[index] = total_items[index];
	}
}

    window.onload = function() {
        var line = document.getElementById("line").getContext("2d");
	var pie = document.getElementById("pie").getContext("2d");
	// set the graph data for plotting
	//setGraphData();

	Chart.defaults.global.legend.display = false;
   	
	window.Line = Chart.Line(line, line_chart_config);
	window.Pie = new Chart(pie, pie_chart_config);
    	//draw_bar_graph();
    };

//graph main ends
