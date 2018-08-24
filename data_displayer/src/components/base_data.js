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

    const prepAltaData = alta.map((val) => {
    return {x: new Date(val.crawled_at), y: val.base_total }
   });  

    const prepSnowbirdData = snowbird.map((val) => {
    return {x: new Date(val.crawled_at), y: val.base_total }
   });    

    const prepSolitudeData = solitude.map((val) => {
    return {x: new Date(val.crawled_at), y: val.base_total }
   });    

    const prepBrightonData = brighton.map((val) => {
    return {x: new Date(val.crawled_at), y: val.base_total }
   });    

    const prepParkCityData = parkCity.map((val) => {
    return {x: new Date(val.crawled_at), y: val.base_total }
   });    

    const prepDeerValleyData = deerValley.map((val) => {
    return {x: new Date(val.crawled_at), y: val.base_total }
   });

    function prepBaseData(array) {
       return array.map((val) => {
            return {x: new Date(val.crawled_at), y: val.base_total }
        })
    };

    // northern utah ski areas

    const prepSnowBasinData = prepBaseData(snowBasin);

    const powderMountainBaseData = prepBaseData(powderMountain);

    const beaverMountainBaseData = prepBaseData(beaverMountain);

    const cherryPeakBaseData = prepBaseData(cherryPeak);

    const nordicValleyBaseData = prepBaseData(nordicValley);

    // cental utah ski areas

    const sundanceBaseData = prepBaseData(sundance);

    // southern utah ski areas

    const brianHeadBaseData = prepBaseData(brianHead);

    const eaglePointBaseData = prepBaseData(eaglePoint);



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
                data={prepAltaData}
        /> 

        <VictoryLine 
                style={{
                    data: { stroke: "#00CD22" }
                    }}
                data={prepSnowbirdData}
        />       

        <VictoryLine 
                style={{
                    data: { stroke: "#FFFF33" }
                    }}
                data={prepSolitudeData}
        />        
        
        <VictoryLine 
                style={{
                    data: { stroke: "#CC0000" }
                    }}
                data={prepBrightonData}
        />        

        <VictoryLine 
                style={{
                    data: { stroke: "#990000" }
                    }}
                data={prepParkCityData}
        />        

        <VictoryLine 
                style={{
                    data: { stroke: "#009900" }
                    }}
                data={prepDeerValleyData}
        />        

        <VictoryLine 
                style={{
                    data: { stroke: "#ffcc00" }
                    }}
                data={prepSnowBasinData}
        />        

        <VictoryLine 
                style={{
                    data: { stroke: "#6699ff" }
                    }}
                data={powderMountainBaseData}
        />        

        <VictoryLine 
                style={{
                    data: { stroke: "#990033" }
                    }}
                data={cherryPeakBaseData}
        />       

        <VictoryLine 
                style={{
                    data: { stroke: "#33334d" }
                    }}
                data={nordicValleyBaseData}
        />         

        <VictoryLine 
                style={{
                    data: { stroke: "#cc3300" }
                    }}
                data={beaverMountainBaseData}
        />  

        <VictoryLine 
                style={{
                    data: { stroke: "#993333" }
                    }}
                data={sundanceBaseData}
        />        

        <VictoryLine 
                style={{
                    data: { stroke: "#006600" }
                    }}
                data={brianHeadBaseData}
        />        

        <VictoryLine 
                style={{
                    data: { stroke: "#336600" }
                    }}
                data={eaglePointBaseData}
        />


        </VictoryChart>
        </div>
        );
}


export default BaseData;

