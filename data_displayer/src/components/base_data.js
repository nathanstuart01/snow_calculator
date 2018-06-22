import React from 'react';

class BaseData extends React.Component {

	baseDataApi = "http://127.0.0.1:5000/api/v1/basedata/";

	render() {
    	return (
      		<div>
      		<p>All the great base data!!!</p>
      		</div>
    	);
  	}
}

export default BaseData;