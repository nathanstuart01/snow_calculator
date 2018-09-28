import React from 'react';
import {VictoryLine, VictoryChart, VictoryGroup, VictorySharedEvents,
        VictoryAxis, VictoryLabel, VictoryLegend, VictoryCursorContainer, VictoryBar} from 'victory';

const BarBaseData = props => {

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

    // currrent data for display purposes
    const todaysDate = new Date();

    // areas in an array for data display purposes

    const tickValues = [
    'Alta', 'Snowbird', 'Brighton', 'Solitude', `Park\nCity`, `Deer\nValley`, `Snow\nBasin`, `Powder\nMountain`, 
    `Beaver\nMountain`, `Cherry\nPeak`, `Brian\nHead`, `Eagle\nPoint`, 'Sundance', `Nordic\nValley`
    ]

    const sampleData = [
    {x: 'Alta', y:30},
    {x: 'Snowbird', y:28},
    {x: 'Solitude', y:20},
    {x: 'Brighton', y:20},
    ]

    const allAreasBaseDataprops = [];

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
            scale={{y: "linear"}}
            domain={{y:[0,150]}}
            width={800}
            padding={{top: 50, bottom:50, left:50 , right: 50}}
        >
        <VictoryLabel text="Current Base Depth Utah Ski Area's 2018-2019" x={375} y={35} textAnchor="middle"/>     
        <VictoryAxis dependentAxis style={{ tickLabels: {fontSize: 10}, ticks: {stroke: "black", size: 3}, axisLabel: { fontSize: 12, padding: 38 }}} label='Depth in Inches' />
        <VictoryAxis  /> 
        <VictoryBar   
        data={sampleData}
        />



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


export default BarBaseData;

