import React from 'react';
import ForecastedSnowData from './forecasted_snow_data';
import BaseData from './base_data';
import TwentyFourHourData from './twenty_four_hour_data';



class App extends React.Component {

  // this is a local state object that can be accessed later with this
  // can only change this through setState()
  state = {
    error: null,
    twentyFourHourData: [],
    forecastedSnowData: [],
    alta: [],
    snowbird: [],
    solitude: [],
    brighton: [],
    'park city': [],
    'deer valley': [],
    'snowbasin': [],
    'powder mountain': [],
    'beaver mountain': [],
    'cherry peak': [],
    'brian head': [],
    'eagle point': [],
    'sundance': [],
    'nordic valley': [],
  }

  getDataToFetch = (urlsToFetch) => {
    for (let i = 0; i < urlsToFetch.length; i ++) {
          this.loadData(urlsToFetch[i])
    }

  }

  loadData = (urlToLoad) => {

    const baseTotalUrl = 'http://localhost:5000/api/v1/basedata/';
    const twentyFourHourTotalUrl = 'http://127.0.0.1:5000/api/v1/twentyfourhourdata/';
    const altaBaseData = 'http://localhost:5000/api/v1/basedata/alta';

    fetch(urlToLoad)
      .then(res => res.json())
      .then(
        (result) => {
          let area = result[0]['area_name']
          console.log(area)
          this.setState({
              [area]: result
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
      const baseDataUrls = [
        'http://localhost:5000/api/v1/basedata/alta',
        'http://localhost:5000/api/v1/basedata/snowbird',
        'http://localhost:5000/api/v1/basedata/solitude',
        'http://localhost:5000/api/v1/basedata/brighton',
        'http://localhost:5000/api/v1/basedata/park city',
        'http://localhost:5000/api/v1/basedata/deer valley',
        'http://localhost:5000/api/v1/basedata/powder mountain',
        'http://localhost:5000/api/v1/basedata/snowbasin',
        'http://localhost:5000/api/v1/basedata/beaver mountain',
        'http://localhost:5000/api/v1/basedata/cherry peak',
        'http://localhost:5000/api/v1/basedata/eagle point',
        'http://localhost:5000/api/v1/basedata/brian head',
        'http://localhost:5000/api/v1/basedata/sundance',
        'http://localhost:5000/api/v1/basedata/nordic valley',
      ]
      this.getDataToFetch(baseDataUrls);
    }
 

	render() {

    	return (
      		<div>
      			<TwentyFourHourData />
            {/* this.state.baseData.length > 0 ? <BaseData data={this.state.baseData} /> : null */}
          </div>
    	);
  	}
}

export default App;
