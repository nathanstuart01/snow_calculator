import React from 'react';
import {VictoryLine, VictoryChart, VictoryAxis, VictoryLabel, VictoryLegend } from 'victory';

const BaseData = props => {

    console.log(props.data);
    const practiceBaseTotal = props.data[0]['base_total'];
    const practiceCrawledAltaDate = props.data[0]['crawled_at'];
    const practiceBaseTotal2 = props.data[1]['base_total'];
    const practiceCrawledAltaDate2 = props.data[1]['crawled_at'];


    const date1 = new Date(practiceCrawledAltaDate);
    const date2 = new Date(practiceCrawledAltaDate2);

    const tickValues = getTickValues();

    function getTickValues() {
        return [ 
        new Date('2018-03-01'), 
        new Date('2018-04-01'), 
        new Date('2018-05-01')

        ]
    }

    return (
        <div>
        <VictoryChart
            scale={{x: "time", y: "linear"}}
            domain={{y:[0,150]}}
        >
    {/*Maybe make the victory legend its own element as a standalone div next to base totals line graph*/ }
     {/*   <VictoryLegend x={125} y={50}
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
        />*/}
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
                    return `03-01\n2018`;
                } else if (x.getMonth() === 2) {
                    return `04-01\n2018`; 
                } else {
                    return `05-01\n2018`;
                }
        }}
        />
            <VictoryLine 
                style={{
                    data: { stroke: "#0000FF" }
                    }}
                data={[
                    {x:date2, y:practiceBaseTotal2},
                    {x:date1, y:practiceBaseTotal},
                ]}
            />
        </VictoryChart>
        </div>
        );
}


export default BaseData;

