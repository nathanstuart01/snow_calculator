import React from 'react';
import {VictoryChart, VictoryAxis, VictoryLabel, VictoryBar, VictoryVoronoiContainer, VictoryTheme } from 'victory';

const BarBaseData = props => {

    const baseData = props.data.map((d) => {
        return {x: d.area_name, y: d.base_total }
    });

    return (

        <div id='baseChart'>
    

       <VictoryChart
            scale={{y: "linear"}}
            domain={{y:[0,150]}}
            width={800}
            padding={{top: 50, bottom:50, left:50 , right: 50}}
              containerComponent={
                    <VictoryVoronoiContainer
                        labels={(d) => `${d.y} in`}
                        radius={15}
                    />
                }
        >
        <VictoryLabel text="Current Base Depth Utah Ski Area's 2018-2019" x={375} y={35} textAnchor="middle"/>     
        <VictoryAxis dependentAxis style={{ tickLabels: {fontSize: 10}, ticks: {stroke: "black", size: 3}, axisLabel: { fontSize: 12, padding: 38 }}} label='Depth in Inches (in)' />
        <VictoryAxis  /> 
        <VictoryBar 
        data={baseData}
        style={{ data: { fill: "#c43a31" , stroke: "black", strokeWidth: 2} }}
        labelComponent={<VictoryLabel dy={25}/>}
        />       
      
        </VictoryChart>
        </div>

        );
}


export default BarBaseData;

