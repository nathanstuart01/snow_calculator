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

    const allAreasBaseDataprops = [];

    const tickValues = getTickValues();

        // northern utah ski areas

    const prepSnowBasinBaseData = prepBaseData(snowBasin);

    const prepPowderMountainBaseData = prepBaseData(powderMountain);

    const prepBeaverMountainBaseData = prepBaseData(beaverMountain);

    const prepCherryPeakBaseData = prepBaseData(cherryPeak);

    const prepNordicValleyBaseData = prepBaseData(nordicValley);

    // cottonwood ski areas

    const prepAltaBaseData = prepBaseData(alta);

    const prepSnowbirdBaseData = prepBaseData(snowbird);
    
    const prepSolitudeBaseData = prepBaseData(solitude);

    const prepBrightonBaseData = prepBaseData(brighton);

    // park city ski areas

    const prepParkCityBaseData = prepBaseData(parkCity);

    const prepDeerValleyBaseData = prepBaseData(deerValley);

    // cental utah ski areas

    const prepSundanceBaseData = prepBaseData(sundance);

    // southern utah ski areas

    const prepBrianHeadBaseData = prepBaseData(brianHead);

    const prepEaglePointBaseData = prepBaseData(eaglePoint);

    function pushBaseDataIntoArray(array) {
        array.push(alta, snowbird, brighton, solitude, parkCity, deerValley,
                    snowBasin, powderMountain, beaverMountain, cherryPeak,
                    nordicValley, sundance, brianHead, eaglePoint
            )
    }

    function testPrepBaseData(array) {
        for ( var i = 0; i < array.length; i ++ ) {
            for ( var x = 0; x < array[i].length; x ++) {
                return {x: new Date(array[i][x]['crawled_at']), y: array[i][x]['base_total']}
                }
            }
        }


    function getTickValues() {
        return [ 
            new Date('2018-03-01'), 
            new Date('2018-04-01'), 
            new Date('2018-05-01')
        ]
    };

    function prepBaseData(array) {
       return array.map((val) => {
            return {x: new Date(val.crawled_at), y: val.base_total }
        })
    };

    function returnBaseDataComponent(lineColor, data) {
 
        return  <VictoryLine style={{ data: { stroke: lineColor } }} data={data} />        
    };

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

        {returnBaseDataComponent('#000000',prepAltaBaseData)}
        {returnBaseDataComponent('#00CD22',prepSnowbirdBaseData)}
        {returnBaseDataComponent('#FFFF33',prepSolitudeBaseData)}
        {returnBaseDataComponent('#CC0000',prepBrightonBaseData)}
        {returnBaseDataComponent('#990000',prepParkCityBaseData)}
        {returnBaseDataComponent('#009900',prepDeerValleyBaseData)}
        {returnBaseDataComponent('#ffcc00',prepSnowBasinBaseData)}
        {returnBaseDataComponent('#6699ff',prepPowderMountainBaseData)}
        {returnBaseDataComponent('#990033',prepCherryPeakBaseData)}
        {returnBaseDataComponent('#33334d',prepNordicValleyBaseData)}
        {returnBaseDataComponent('#cc3300',prepBeaverMountainBaseData)}
        {returnBaseDataComponent('#993333',prepSundanceBaseData)}
        {returnBaseDataComponent('#006600',prepBrianHeadBaseData)}
        {returnBaseDataComponent('#336600',prepEaglePointBaseData)}
        {pushBaseDataIntoArray(allAreasBaseDataprops)}    
        {testPrepBaseData(allAreasBaseDataprops)}        


        </VictoryChart>
        </div>
        );
}


export default BaseData;

