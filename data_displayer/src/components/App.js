import React from 'react';
import ForecastedSnowData from './forecasted_snow_data';
import BaseData from './base_data';
import TwentyFourHourData from './twenty_four_hour_data';



class App extends React.Component {

  // this is a local state object that can be accessed later with this
  // can only change this through setState()
  state = {
    error: null,
    isLoadingBaseData: false,
    isLoadingTwentyFourData: false,
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
    'nordic valley': []
  }

  getDataToFetch = (urlsToFetch) => {
    for (let i = 0; i < urlsToFetch.length; i ++) {
          this.loadBaseData(urlsToFetch[i])
    }

  }

  loadBaseData = (urlToLoad) => {

    fetch(urlToLoad)
      .then(res => res.json())
      .then(
        (result) => {
          let area = result[0]['area_name']
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
      .then(
         () => {
          this.setState({
            isLoadingBaseData: false
          }) 
         } 
        )
    }

    getTwentyFourHourdata = (urlToLoad) => {

    fetch(urlToLoad)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            twentyFourHourData: result, isLoadingTwentyFourData: false
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
      ];

      const twentyFourHourTotalUrl = 'http://127.0.0.1:5000/api/v1/twentyfourhourdata/';

      this.setState({ isLoadingBaseData: true, isLoadingTwentyFourData: true });

      this.getDataToFetch(baseDataUrls);

      this.getTwentyFourHourdata(twentyFourHourTotalUrl);
    }
    
    
	render() {

    const { isLoadingBaseData, isLoadingTwentyFourData } = this.state;

    if (isLoadingBaseData || isLoadingTwentyFourData) {
      return <p>Loading Area Data....</p>;
    }

    	return (
      		<div>
              <div id='twentyFourHourDataDiv'>
        			   {this.state.twentyFourHourData. length  > 0 ? <TwentyFourHourData data={this.state.twentyFourHourData} /> : null }
              </div>
              <div id='baseDataDiv'>
                 { this.state['nordic valley'].length > 0 ? <BaseData 
                 alta={this.state.alta} snowbird={this.state.snowbird} 
                 solitude={this.state.solitude} brighton={this.state.brighton}
                 deerValley={this.state['deer valley']} parkCity={this.state['park city']}
                 snowBasin={this.state.snowbasin} powderMountain={this.state['powder mountain']}
                 beaverMountain={this.state['beaver mountain']} cherryPeak={this.state['cherry peak']}
                 eaglePoint={this.state['eagle point']} brianHead={this.state['brian head']}
                 nordicValley={this.state['nordic valley']} sundance={this.state.sundance}
             /> : null }
             </div>
          </div>
    	);
  	}
}

export default App;
