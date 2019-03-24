import React from 'react';
import {VictoryChart, VictoryAxis, VictoryLabel, VictoryBar, VictoryVoronoiContainer } from 'victory';

const BarTwentyFourHourData = props => {

    const twentyFourHourData = props.data.map((d) => {
        return {x: d.area_name, y: d.twenty_four_hour_total }
    });

    let currentDate = new Date().toLocaleString();

    let twentyFourMessage = "Twenty Four Hour Snow Fall Totals at Utah Ski Areas as of: " + currentDate

    return (

        <div>
    
       <VictoryChart
            scale={{y: "linear"}}
            domain={{y:[0,30] }}
            domainPadding={{x:[15, 15]}}
            width={800}
              containerComponent={
                    <VictoryVoronoiContainer
                        labels={(d) => `${d.y} in`}
                        radius={15}
                    />
                }

        >
        <VictoryLabel text={twentyFourMessage} x={375} y={35} textAnchor="middle"/>     
        <VictoryAxis dependentAxis style={{ 
            tickLabels: {fontSize: 10}, 
            grid: {stroke: "grey", size: 5}, 
            axisLabel: { fontSize: 11, padding:30 }
            }}
            label='24hr Snowfall in Inches' />
        <VictoryAxis style={{ tickLabels: { angle: -20, fontSize: 10, padding: 10 }}}  /> 
        <VictoryBar
        data={twentyFourHourData} 
        style={{ 
            data: { fill: "#c43a31" , stroke: "black", strokeWidth: 2},
            }}
        />       
      
        </VictoryChart>
        </div>

        );
}


export default BarTwentyFourHourData;