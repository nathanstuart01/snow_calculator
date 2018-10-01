import React from 'react';
import {VictoryLine, VictoryChart, VictoryGroup, VictorySharedEvents,
        VictoryAxis, VictoryLabel, VictoryLegend, VictoryCursorContainer, VictoryBar} from 'victory';

const BarBaseData = props => {

    const alta = props.alta.slice(-1)[0];
    const snowbird = props.snowbird.slice(-1)[0];
    const brighton = props.brighton.slice(-1)[0];
    const solitude = props.solitude.slice(-1)[0];
    const parkCity = props.parkCity.slice(-1)[0];
    const deerValley = props.deerValley.slice(-1)[0];
    const snowBasin = props.snowBasin.slice(-1)[0];
    const powderMountain = props.powderMountain.slice(-1)[0];
    const beaverMountain = props.beaverMountain.slice(-1)[0];
    const cherryPeak = props.cherryPeak.slice(-1)[0];
    const brianHead = props.brianHead.slice(-1)[0];
    const eaglePoint = props.eaglePoint.slice(-1)[0];
    const sundance = props.sundance.slice(-1)[0];
    const nordicValley = props.nordicValley.slice(-1)[0];

    return (

        <div id='baseChart'>
    

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
        style={{
            data: { fill: "#c43a31" }
            }}   
        data={[
            {x: alta['area_name'], y: alta['base_total']}]}
        />       
         <VictoryBar
        style={{
            data: { fill: "#c43a31" }
            }}   
        data={[
            {x: snowbird['area_name'], y: snowbird['base_total']}]}
        />        
        <VictoryBar
        style={{
            data: { fill: "#c43a31" }
            }}   
        data={[
            {x: solitude['area_name'], y: solitude['base_total']}]}
        />        
        <VictoryBar
        style={{
            data: { fill: "#c43a31" }
            }}   
        data={[
            {x: brighton['area_name'], y: brighton['base_total']}]}
        />        
        <VictoryBar
        style={{
            data: { fill: "#c43a31" }
            }}   
        data={[
            {x: parkCity['area_name'], y: parkCity['base_total']}]}
        />        
        <VictoryBar
        style={{
            data: { fill: "#c43a31" }
            }}   
        data={[
            {x: deerValley['area_name'], y: deerValley['base_total']}]}
        />        
        <VictoryBar
        style={{
            data: { fill: "#c43a31" }
            }}   
        data={[
            {x: snowBasin['area_name'], y: snowBasin['base_total']}]}
        />        
        <VictoryBar
        style={{
            data: { fill: "#c43a31" }
            }}   
        data={[
            {x: powderMountain['area_name'], y: powderMountain['base_total']}]}
        />        
        <VictoryBar
        style={{
            data: { fill: "#c43a31" }
            }}   
        data={[
            {x: beaverMountain['area_name'], y: beaverMountain['base_total']}]}
        />        
        <VictoryBar
        style={{
            data: { fill: "#c43a31" }
            }}   
        data={[
            {x: cherryPeak['area_name'], y: cherryPeak['base_total']}]}
        />        
        <VictoryBar
        style={{
            data: { fill: "#c43a31" }
            }}   
        data={[
            {x: nordicValley['area_name'], y: nordicValley['base_total']}]}
        />       
        <VictoryBar
        style={{
            data: { fill: "#c43a31" }
            }}   
        data={[
            {x: sundance['area_name'], y: sundance['base_total']}]}
        />        
        <VictoryBar
        style={{
            data: { fill: "#c43a31" }
            }}   
        data={[
            {x: eaglePoint['area_name'], y: eaglePoint['base_total']}]}
        />        
        <VictoryBar
        style={{
            data: { fill: "#c43a31" }
            }}   
        data={[
            {x: brianHead['area_name'], y: brianHead['base_total']}]}
        />        
        </VictoryChart>
        </div>

        );
}


export default BarBaseData;

