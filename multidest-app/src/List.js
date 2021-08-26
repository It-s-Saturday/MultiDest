import logo from './logo.svg';
import React from 'react';
// import './App.css';

const textAreaStyles = {
	  width: 235,
	  margin: 5
	};

class List extends React.Component{
  constructor(props) {
	    super(props);
	    // Change code below this line
	    this.state = {
	      userInput: "",
        originInput: "",
        destinationInput: "",
	      list: []
	    }
	    // Change code above this line
	    this.handleSubmit = this.handleSubmit.bind(this);
	    this.handleChange = this.handleChange.bind(this);
      this.handleOriginChange = this.handleOriginChange.bind(this);
      this.handleDestinationChange = this.handleDestinationChange.bind(this);
	  }
	  handleSubmit() {
	    this.setState({
	      list: this.state.list.concat(this.state.userInput),
        userInput: ""
	    });
	  }
	  handleChange(e) {
	    this.setState({
	      userInput: e.target.value
	    });
	  }

    handleOriginChange(e) {
      let origin_array = this.state.list.slice();
      this.setState({
        originInput: e.target.value,
        list: [e.target.value].concat(this.state.list.slice(1, this.state.list.length)).filter(element => element != "")
      });
    }

    handleDestinationChange(e) {

      // var destination = {...this.state.list[this.state.list.length-1]};
      this.setState({
        destinationInput: e.target.value,
        list: [...this.state.list.slice(0, this.state.list.length+1)].concat([e.target.value]).filter(element => element != "")
      });
    }


	  render() {
	    const items = this.state.list.map(i => <li>{i}</li>)
	    return (
	      <div>
          <input type="text" placeholder="origin" value={this.state.originInput} style={textAreaStyles} onChange={this.handleOriginChange} />
          <br />
          <form onSubmit={this.handleSubmit} action="javascript:void(0);">
            <div>
              <input type ="radio" id="distance" name="optimize_for" value="distance" />
              <label for="distance_choice">distance</label>
              <input type ="radio" id="timeout" name="optimize_for" value="time" />
              <label for="time_choice">time</label>
              </div>
            <br/>
            <textarea
  	          onChange={this.handleChange}
  	          value={this.state.userInput}
  	          style={textAreaStyles}
  	          placeholder=''
              required
  	        />
  	        <button type="submit">Add to list</button>
            <br />
          </form>
          <input type="text" placeholder="destination" value={this.state.destinationInput} style={textAreaStyles} onChange={this.handleDestinationChange} />
	        <ol>{items}</ol>
	      </div>
	    );
	  }

}
export default List;
