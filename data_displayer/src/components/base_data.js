import React from 'react';
import {XYPlot, XAxis, YAxis, VerticalGridLines, HorizontalGridLines, LineSeries} from 'react-vis';

const BaseData = (props) => {

	const baseData = props.baseData.map((area) => <li>area.area_name</li>);

		return (
			<div>
			<h2>Base Data</h2>
			<h2>{baseData}</h2>
            <XYPlot
                width={300}
                height={300}>
                <VerticalGridLines />
                <HorizontalGridLines />
                <XAxis />
                <YAxis />
                <LineSeries data={[
                				{x: 1, y: 2},
                				{x: 2, y: 3}
                				]}/>
                <LineSeries data={[
                				{x: 4, y: 5},
                				{x: 5, y: 6}
                				]}/>
            </XYPlot>
            </div>
        );

}

export default BaseData;