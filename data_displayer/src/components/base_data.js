import React from 'react';
import {VictoryLine, VictoryChart, VictoryAxis, VictoryLabel, VictoryLegend } from 'victory';

const BaseData = props => {

    const alta = props.alta;
    const snowbird = props.snowbird;
    const brighton = props.brighton;
    const solitude = props.solitude;
    const parkCity = props.parkCity;
    const deerValley = props.deerValley;
    const snowBasin = props.snowBasin;
    const powderMountain = props.powderMountain;
    const beaverMountain = props.beaverMountain;
    const cherryPeak = props.cherryPeak;
    const brianHead = props.brianHead;
    const eaglePoint = props.eaglePoint;
    const sundance = props.sundance;
    const nordicValley = props.nordicValley;

    const tickValues = getTickValues();

    function getTickValues() {
        return [ 
        new Date('2018-03-01'), 
        new Date('2018-04-01'), 
        new Date('2018-05-01')
        ]
    }

   const prepBaseData = snowbird.map((val) => {
    return {x: new Date(val.crawled_at), y: val.base_total }
   });

   console.log(prepBaseData)

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
                data={prepBaseData}
            />
        </VictoryChart>
        </div>
        );
}


export default BaseData;

