import React from 'react';
import ForecastedSnowData from './forecasted_snow_data';
import BaseData from './base_data';
import TwentyFourHourData from './twenty_four_hour_data';



class App extends React.Component {

  // this is a local state object that can be accessed later with this
  // can only change this through setState()
  state = {
    error: null,
    baseData: [],
    twentyFourHourData: [],
    forecastedSnowData: []
  }

  componentDidMount() {
    // set these as consts because they will not change in the future 
    const twentyFourHourTotalUrl = 'http://127.0.0.1:5000/api/v1/twentyfourhourdata/';
    const baseTotalUrl = 'http://localhost:5000/api/v1/basedata/';

    
    fetch(twentyFourHourTotalUrl)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            twentyFourHourData: result
          });
        },
        (error) => {
          this.setState({
            error
          });
        }
      )

    fetch(baseTotalUrl)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            baseData: result
          });
        },
        (error) => {
          this.setState({
            error
          });
        }
      )
    }

	render() {

    	return (
      		<div>
      			<ForecastedSnowData />
      			<BaseData baseData={this.state.baseData}/>
      			<TwentyFourHourData />
      		</div>
    	);
  	}
}

export default App;
