import React from 'react';
import {VictoryLine, VictoryChart, VictoryAxis, VictoryLabel, VictoryLegend } from 'victory';

const BaseData = props => {

    const practiceBaseTotal = props.data[0]['base_total'];
    console.log(props.data[0]['crawled_at']);

    const date1 = new Date('2018-11-01');
    const date2 = new Date('2019-05-01');
    const date3 = new Date('2018-11-25');
    const date4 = new Date('2018-11-26');
    const date5 = new Date('2018-11-27');
    const date6 = new Date('2018-11-28');
    const date7 = new Date('2018-11-29');
    const date8 = new Date('2018-12-15');
    const date9 = new Date('2019-02-15');
    const date10 = new Date('2019-03-01');

    const tickValues = getTickValues();

    function getTickValues() {
        return [ 
        new Date('2018-11-01'), 
        new Date('2018-12-01'), 
        new Date('2019-01-01'), 
        new Date('2019-02-01'), 
        new Date('2019-03-01'), 
        new Date('2019-04-01'), 
        new Date('2019-05-01') 
        ]
    }

    return (
        <div>
        <VictoryChart
            scale={{x: "time", y: "linear"}}
            domain={{y:[0,150]}}
        >
    {/*Maybe make the victory legend its own element as a standalone div next to base totals line graph*/ }
        <VictoryLegend x={125} y={50}
        title="Ski Areas"
        centerTitle
        orientation="horizontal"
        gutter={30}
        style={{ border: { stroke: "black" }, title: {fontSize: 20 } }}
        itemsPerRow={4}
        data={[
          { name: "Alta", symbol: { fill: "#0000FF"} },
          { name: "Brighton", symbol: { fill: "orange" } },
          { name: "Snowbird", symbol: { fill: "gold" } }
        ]}
        />
        <VictoryLabel text="Base Totals for Utah Ski Area's for 2018-2019" x={225} y={30} textAnchor="middle"/>     
        <VictoryAxis dependentAxis style={{ axisLabel: { padding: 35 }}} label='Base Depth (in)' />
        <VictoryAxis   scale="time" style={{ tickLabels: { angle: -50 } }} tickLabelComponent={<VictoryLabel />} tickValues={tickValues} tickFormat={ (x) => { 
                if (x.getMonth() === 9) {
                    return `11-01\n2018`;
                } else if (x.getMonth() === 10) {
                    return `12-01\n2018`;
                } else if (x.getMonth() === 11) {
                    return `01-01\n2019`;
                } else if (x.getMonth() === 0) {
                    return `02-01\n2019`;
                } else if (x.getMonth() === 1) {
                    return `03-01\n2019`;
                } else if (x.getMonth() === 2) {
                    return `04-01\n2019`; 
                } else {
                    return `05-01\n2019`;
                }
        }}
        />
            <VictoryLine 
                style={{
                    data: { stroke: "#0000FF" }
                    }}
                data={[
                    {x:date3, y:30},
                    {x:date4, y:40},
                    {x:date5, y:45},
                    {x:date6, y:50},
                    {x:date7, y:60},
                    {x:date8, y:75},
                    {x:date9, y:100},
                    {x:date10, y:0},
                ]}
            />
        </VictoryChart>
        </div>
        );
}


export default BaseData;

