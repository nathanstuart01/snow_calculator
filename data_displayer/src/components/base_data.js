import React from 'react';
import {VictoryLine, VictoryChart, VictoryGroup, VictorySharedEvents,
        VictoryAxis, VictoryLabel, VictoryLegend, VictoryCursorContainer} from 'victory';

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

    const legendValues = getLegendValues();

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

    function getTickValues() {
        return [ 
            new Date('2018-03-01 GMT-0700'), 
            new Date('2018-03-15 GMT-0700'), 
            new Date('2018-04-01 GMT-0700'), 
            new Date('2018-04-15 GMT-0700'), 
            new Date('2018-05-01 GMT-0700')
        ]
    };

    function getLegendValues() {
        return[
            { name: "Alta", symbol: { fill: "#e6194B", type: 'minus'} },
          { name: "Snowbird", symbol: { fill: "#3cb44b", type: 'minus' } },
          { name: "Brighton", symbol: { fill: "#ffe119", type: 'minus' } },
          { name: "Solitude", symbol: { fill: "#4363d8", type: 'minus' } },
          { name: "Park City ", symbol: { fill: "#f58231", type: 'minus' } },
          { name: "Deer Valley", symbol: { fill: "#911eb4", type: 'minus' } },
          { name: "Snowbasin", symbol: { fill: "#42d4f4", type: 'minus' } },
          { name: "Powder Mtn.", symbol: { fill: "#6699ff", type: 'minus' } },
          { name: "Beaver Mtn.", symbol: { fill: "#cc3300", type: 'minus' } },
          { name: "Cherry Peak", symbol: { fill: "#990033", type: 'minus' } },
          { name: "Nordic Valley", symbol: { fill: "#33334d", type: 'minus' } },
          { name: "Sundance", symbol: { fill: "#9A6324", type: 'minus' } },
          { name: "Brian Head", symbol: { fill: "#006600", type: 'minus' } },
          { name: "Eagle Point", symbol: { fill: "#336600", type: 'minus' } },
          ]
    };

    function prepBaseData(array) {
       return array.map((val) => {
            return {x: new Date(val.crawled_at), y: val.base_total }
        })
    };

    function returnBaseDataComponent(lineColor, data, areaName) {
        return <VictoryLine style={{ data: { stroke: lineColor } }} data={data} name={areaName} />
    };

    return (

        <div id='baseChart'>
        {pushBaseDataIntoArray(allAreasBaseDataprops)}

       <VictoryChart
            scale={{x: "time", y: "linear"}}
            domain={{y:[0,150]}}
            width={800}
            padding={{top: 50, bottom:50, left:50 , right: 50}}
            containerComponent={
                <VictoryCursorContainer
                    cursorDimension="x"
                    cursorLabel={(d) => `${Math.round(d.y, 1)} in, ${d.x.toLocaleDateString()}  `}
                />}
        >
        <VictoryLabel text="Base Depths Utah Ski Area's 2018-2019" x={375} y={35} textAnchor="middle"/>     
        <VictoryAxis dependentAxis style={{ tickLabels: {fontSize: 10}, ticks: {stroke: "black", size: 3}, axisLabel: { fontSize: 12, padding: 38 }}} label='Base Depth (in)' />
        <VictoryAxis   scale="time" style={{ tickLabels: { angle: 0, fontSize: 10}, ticks: {stroke: "black", size: 3} }} tickLabelComponent={<VictoryLabel />} tickValues={tickValues} tickFormat={ (x) => { 
                return x.toLocaleDateString();
            }}
        />

        {returnBaseDataComponent('#e6194B',prepAltaBaseData, 'altaLine')}
        {returnBaseDataComponent('#3cb44b',prepSnowbirdBaseData, 'snowbirdLine')}
        {returnBaseDataComponent('#4363d8',prepSolitudeBaseData, 'solitudeLine')}
        {returnBaseDataComponent('#ffe119',prepBrightonBaseData, 'brightonLine')}
        {returnBaseDataComponent('#f58231',prepParkCityBaseData, 'parkCityLine')}
        {returnBaseDataComponent('#911eb4',prepDeerValleyBaseData, 'deerValleyLine')}
        {returnBaseDataComponent('#42d4f4',prepSnowBasinBaseData, 'snowBasinLine')}
        {returnBaseDataComponent('#6699ff',prepPowderMountainBaseData, 'powderMountainLine')}
        {returnBaseDataComponent('#990033',prepCherryPeakBaseData, 'cherryPeakLine')}
        {returnBaseDataComponent('#33334d',prepNordicValleyBaseData, 'nordicValleyLine')}
        {returnBaseDataComponent('#cc3300',prepBeaverMountainBaseData, 'beaverMountainLine')}
        {returnBaseDataComponent('#9A6324',prepSundanceBaseData, 'sundanceLine')}
        {returnBaseDataComponent('#006600',prepBrianHeadBaseData, 'brianHeadLine')}
        {returnBaseDataComponent('#336600',prepEaglePointBaseData, 'eaglePointLine')}

        </VictoryChart>
        <div id='baseLegend'>
        <VictoryLegend 
        orientation="horizontal"
        width={900}
        style={{ border: { stroke: "black" }, labels: {fontSize: 16} }}
        itemsPerRow={7}
        data={legendValues}
        />
        </div>
        </div>

        );
}


export default BaseData;

