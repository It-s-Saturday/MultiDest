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
        stops: 0,
        originInput: "",
        origincount: 0,
        originTrue: false,
        destinationInput: "",
        destinationcount: 0,
        expected_length: 0,
        destination_set: false,
	      list: [],

        destination_hidden: true,
        optimize_hidden: true
	    }
	    // Change code above this line
	    this.handleSubmit = this.handleSubmit.bind(this);
	    this.handleChange = this.handleChange.bind(this);
      this.handleOriginChange = this.handleOriginChange.bind(this);
      this.handleDestinationChange = this.handleDestinationChange.bind(this);

	  }
	  handleSubmit() {
      let copy = this.state.list.slice();
      let last_element = copy[-1];
      // const t = this.state.userInput.split("\n");
      if (copy.length <= 1 || !this.state.destination_set) {
        this.setState({
          // list: t,
  	      // list: this.state.list.concat(this.state.userInput),
          list: copy.concat(this.state.userInput),
          userInput: "",
          expected_length: this.state.expected_length + 1
  	    });
      }
      else {
  	    this.setState({
          // list: t,
  	      // list: this.state.list.concat(this.state.userInput),
          list: [...this.state.list.slice(0, this.state.list.length-1), this.state.userInput, ...this.state.list.slice(this.state.list.length-1)].filter(element => element != ""),
          userInput: "",
          expected_length: this.state.expected_length + 1
  	    });
      }
	  }

	  handleChange(e) {
      let input_test = -1;
      if (this.state.userInput != "") {
        input_test = 1;
      }
	    this.setState({
        // expected_length: this.state.expected_length + input_test,
	      userInput: e.target.value
	    });
	  }

    handleOriginChange(e) {
      // let origin_array = this.state.list.slice();
      let origin_test = -1;
      if (this.state.destination_set) {
        origin_test = 0;
      }

      if (this.state.originInput != "" && !this.state.destination_set) {
        origin_test = 1;
      }
      if (this.state.originInput == "") {
        this.state.destination_hidden = true;
        origin_test = 0;
      }
      this.setState({
        destination_hidden: false,
        expected_length: this.state.expected_length + origin_test,
        originInput: e.target.value,
        list: [e.target.value].concat(this.state.list.slice(1, this.state.list.length)).filter(element => element != "")
      });
    }

    handleDestinationChange(e) {
      const copy = this.state.list.slice();
      copy.concat([e.target.value]);
      if (!this.state.destination_set) {
        this.state.list = copy;
        this.state.expected_length -= 1;
      }
      this.state.destinationInput = "" ? false : true;
      // var destination = {...this.state.list[this.state.list.length-1]};
      this.setState({
        destination_set: true,
        destinationInput: e.target.value,
        list: [...this.state.list.slice(0, this.state.expected_length), [e.target.value]].filter(element => element != "")
      });
    }


	  render() {
	    const items = this.state.list.map(i => <li>{i}</li>)
	    return (
	      <div>
          <input type="text" placeholder="origin" value={this.state.originInput} style={textAreaStyles} onChange={this.handleOriginChange} />
          <br />
          <form onSubmit={this.handleSubmit} action="javascript:void(0)" > //TODO: add action
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
  	        <button>Add to list</button>
            <br />
            <button hidden={this.state.optimize_hidden} type="submit" id="submit_to_run">Optimize Route</button>
          </form>
          <input hidden={this.state.destination_hidden} type="text" placeholder="destination" value={this.state.destinationInput} style={textAreaStyles} onChange={this.handleDestinationChange} />
	        <ol>{items}</ol>

	      </div>
	    );
	  }

}
export default List;
