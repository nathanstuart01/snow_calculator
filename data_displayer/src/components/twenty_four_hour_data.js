import React from 'react';
import { XYPlot, XAxis, YAxis, HorizontalGridLines, VerticalGridLines, LineSeries } from 'react-vis';
import {curveCatmullRom} from 'd3-shape';


const TwentyFourHourData = (props) => {
	return(
		<div>
		<h2>24 Hr Data</h2>
		<XYPlot
        width={300}
        height={300}>
        <HorizontalGridLines />
        <VerticalGridLines />
        <XAxis position="start"/>
        <YAxis />
        <LineSeries
          className="first-series"
          data={[
            {x: 1, y: 3},
            {x: 2, y: 5}
          ]}/>
      </XYPlot>
      </div>
      );
}

export default TwentyFourHourData;