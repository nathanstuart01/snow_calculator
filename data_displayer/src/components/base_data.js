import React from 'react';
import {XYPlot, XAxis, YAxis, VerticalGridLines, HorizontalGridLines, LineSeries} from 'react-vis';

const BaseData = (props) => {

      const altaDataUpdate = props.baseData[0];
      if (altaDataUpdate) {
        console.log(altaDataUpdate['area_name']);
      } else {
        console.log('no alta data mounted yet in did update');
      }

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
                				{x:3, y:2}
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