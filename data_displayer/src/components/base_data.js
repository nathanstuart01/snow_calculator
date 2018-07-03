import React from 'react';
import {XYPlot, XAxis, YAxis, VerticalGridLines, HorizontalGridLines, LineSeries} from 'react-vis';

const BaseData = (props) => {

		return (
			<div>
			<h2>Base Data</h2>
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
            </XYPlot>
            </div>
        );

}

export default BaseData;