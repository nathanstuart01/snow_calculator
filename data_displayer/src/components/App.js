import React from 'react';
import BarBaseData from './bar_base_data';
import BarTwentyFourHourData from './bar_twenty_four_hour_data';
import BaseDataNotReady from './base_data_not_ready';
import TwentyFourDataNotReady from './twenty_four_data_not_ready';


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

      const baseDataUrl = process.env.REACT_APP_BASE_API_URL;

      const twentyFourHourTotalUrl = process.env.REACT_APP_TWENTY_FOUR_HOUR_API_URL;

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
                {this.state.baseData.length > 0 ? <BarBaseData data={this.state.baseData}/> : <BaseDataNotReady /> }
              </div>
              <div>
                {this.state.twentyFourHourData.length  > 0 ? <BarTwentyFourHourData data={this.state.twentyFourHourData} /> : <TwentyFourDataNotReady /> }
             </div>
          </div>
    	);
  	}
}

export default App;
