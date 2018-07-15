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

  loadData = () => {

    const baseTotalUrl = 'http://localhost:5000/api/v1/basedata/';
    const twentyFourHourTotalUrl = 'http://127.0.0.1:5000/api/v1/twentyfourhourdata/';

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
  }

  componentDidMount() {
      this.loadData();
    }
 

	render() {

    	return (
      		<div>
      			<ForecastedSnowData />
      			<TwentyFourHourData />
            { this.state.baseData.length > 0 ? <BaseData data={this.state.baseData} /> : null }
      		</div>
    	);
  	}
}

export default App;
