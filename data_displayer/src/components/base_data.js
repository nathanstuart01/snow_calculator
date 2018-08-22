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

   function sortBaseData(array) {  
        console.log(array)
    }

    return (

        <div onLoad={sortBaseData(alta)}>
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
                    {x:new Date(alta[0]['crawled_at']), y:alta[0]['base_total']},
                    {x:new Date(alta[1]['crawled_at']), y:alta[1]['base_total']},
                    {x:new Date(alta[2]['crawled_at']), y:alta[2]['base_total']},
                    {x:new Date(alta[3]['crawled_at']), y:alta[3]['base_total']},
                    {x:new Date(alta[4]['crawled_at']), y:alta[4]['base_total']},
                    {x:new Date(alta[5]['crawled_at']), y:alta[5]['base_total']},
                    {x:new Date(alta[6]['crawled_at']), y:alta[6]['base_total']},
                    {x:new Date(alta[7]['crawled_at']), y:alta[7]['base_total']},
                    {x:new Date(alta[8]['crawled_at']), y:alta[8]['base_total']},
                    {x:new Date(alta[9]['crawled_at']), y:alta[9]['base_total']},
                    {x:new Date(alta[10]['crawled_at']), y:alta[10]['base_total']},
                    {x:new Date(alta[11]['crawled_at']), y:alta[11]['base_total']},
                    {x:new Date(alta[12]['crawled_at']), y:alta[12]['base_total']},
                    {x:new Date(alta[13]['crawled_at']), y:alta[13]['base_total']},
                    {x:new Date(alta[14]['crawled_at']), y:alta[14]['base_total']},
                    {x:new Date(alta[15]['crawled_at']), y:alta[15]['base_total']},
                    {x:new Date(alta[16]['crawled_at']), y:alta[16]['base_total']},
                    {x:new Date(alta[17]['crawled_at']), y:alta[17]['base_total']},
                    {x:new Date(alta[18]['crawled_at']), y:alta[18]['base_total']},
                    {x:new Date(alta[19]['crawled_at']), y:alta[19]['base_total']},
                ]}
            />
        </VictoryChart>
        </div>
        );
}


export default BaseData;

