import React from 'react';
import BaseData from './base_data';
import TwentyFourHourData from './twenty_four_hour_data';
import ForecastedSnowData from './forecasted_snow_data';
import LineGraph from './line_graph';
import BarGraph from './bar_graph';

class App extends React.Component {

	state = {
		baseData: [],
		twentyFourHourData: [],
		forecastedSnowData: [],
	};

	render() {
    	return (
      		<div>
      			<BaseData />
      			<TwentyFourHourData />
      			<ForecastedSnowData />
      			<LineGraph />
      			<BarGraph />
      		</div>
    	);
  	}
}

export default App;
