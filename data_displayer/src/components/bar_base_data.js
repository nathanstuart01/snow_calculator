import React from 'react';
import {VictoryChart, VictoryAxis, VictoryLabel, VictoryBar, VictoryVoronoiContainer, VictoryTheme } from 'victory';

const BarBaseData = props => {

    const baseData = props.data.map((d) => {
        return {y: d.base_total }
    });

    const baseLabels = props.data.map((d) => {
        return d.area_name
    })

    return (

        <div id='baseChart'>
    

       <VictoryChart
            scale={{y: "linear"}}
            domain={{y:[0,150]}}
            width={800}
              containerComponent={
                    <VictoryVoronoiContainer
                        labels={(d) => `${d.y} in`}
                        radius={15}
                    />
                }
        >
        <VictoryLabel text="Current Base Depth Utah Ski Area's 2018-2019" x={375} y={35} textAnchor="middle"/>     
        <VictoryAxis dependentAxis style={{ 
            tickLabels: {fontSize: 10}, 
            grid: {stroke: "grey", size: 3}, 
            axisLabel: { fontSize: 12 }
            }} 
            label='Depth in Inches (in)' />
        <VictoryAxis  style={{ tickLabels: { angle: -30, fontSize: 10, padding: 20} }} tickFormat={baseLabels} /> 
        <VictoryBar 
        data={baseData}
        style={{ 
            data: { fill: "#c43a31" , stroke: "black", strokeWidth: 2},
            }}
        />       
      
        </VictoryChart>
        </div>

        );
}


export default BarBaseData;

