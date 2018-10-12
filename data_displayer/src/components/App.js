import React from 'react';
import BarBaseData from './bar_base_data';
import BarTwentyFourHourData from './bar_twenty_four_hour_data';
import DataNotReady from './data_not_ready';



class App extends React.Component {

  state = {
    error: null,
    isLoadingBaseData: false,
    isLoadingTwentyFourData: false,
    twentyFourHourData: [],
    forecastedSnowData: [],
    baseData: []
  }

  getDataToFetch = (urlsToFetch) => {
    for (let i = 0; i < urlsToFetch.length; i ++) {
          this.loadBaseData(urlsToFetch[i])
    }

  }

  getBaseData = (urlToLoad) => {

    fetch(urlToLoad)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
              baseData: result, isLoadingBaseData: false
          });
        },
        (error) => {
          this.setState({
            error
          });
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

      const baseDataUrl = 'http://localhost:5000/api/v1/basedata/';

      const twentyFourHourTotalUrl = 'http://127.0.0.1:5000/api/v1/twentyfourhourdata/';

      this.setState({ isLoadingBaseData: true, isLoadingTwentyFourData: true });

      this.getBaseData(baseDataUrl);

      this.getTwentyFourHourdata(twentyFourHourTotalUrl);
    }
    
    
	render() {

    const { isLoadingBaseData, isLoadingTwentyFourData } = this.state;

    if (isLoadingBaseData || isLoadingTwentyFourData) {
      return <p id='loadingParagraph'>Loading Utah Snowfall Data....</p>;
    }

    	return (
      		<div>
              <div>
                {this.state.baseData.length > 0 ? <BarBaseData data={this.state.baseData}/> : null }
              </div>
              <div>
                {this.state.twentyFourHourData.length  > 0 ? <BarTwentyFourHourData data={this.state.twentyFourHourData} /> : null }
             </div>
             <div>
             {this.state.baseData.length === 0 || this.state.twentyFourHourData.length === 0 ? <DataNotReady /> : null }
             </div>
          </div>
    	);
  	}
}

export default App;
