import logo from './logo.svg';
import React from 'react';
// import './App.css';

const textArea = {
	  width: 235,
		height: 150,
	  margin: 5
	};

class List extends React.Component{
  constructor(props) {
	    super(props);
	    // Change code below this line
	    this.state = {
	      userInput: "",
	      list: [],
        list_set: false,
				choice: "",
				choice_set: false
	    }
	    // Change code above this line
	    this.handleRadio = this.handleRadio.bind(this);
	    this.handleChange = this.handleChange.bind(this);
			this.parseInput = this.parseInput.bind(this);
	  }

		parseInput() {
			const parsed = this.state.userInput.split('\n').filter(e => e != "" );
			if (parsed.length < 4) {
				this.setState({
					list: [],
					list_set: false
				});
			}
			else {
				var visual_parsed = parsed.slice();
				for (var i = 0; i < visual_parsed.length; i++) {
					let t = i;
					if (t == 0) {
						t = "Origin";
					}
					else if (t == visual_parsed.length-1) {
						t = "Destination";
					}
					else {
						t = "Stop " + i;
					}
					visual_parsed[i] = t + ": " + visual_parsed[i];
				}

				this.setState({
					list: visual_parsed,
					list_set: true
				});
			}
		}

	  handleRadio(e) {
			this.setState({
				choice: e.target.value,
				choice_set: true
			});
	  }

	  handleChange(e) {
			this.setState({
				userInput: e.target.value
			});
	  }

	  render() {
	    const items = this.state.list.map(i => <p>{i}</p>)

	    return (
	      <div>

          <br />
          <form onSubmit={this.handleSubmit} action="javascript:void(0)" >
            <div>
              <input onChange={this.handleRadio} type ="radio" id="distance" name="optimize_for" value="distance" />
              <label for="distance_choice">distance</label>
              <input onChange={this.handleRadio} type ="radio" id="timeout" name="optimize_for" value="time" />
              <label for="time_choice">time</label>
              </div>
            <br/>
						<p>
						Enter your route, with each location on a new line.
						</p>
            <textarea
  	          onChange={this.handleChange}
  	          value={this.state.userInput}
  	          style={textArea}
  	          placeholder=''
              required
  	        />
						<br />
  	        <button onClick={this.parseInput}>Parse route</button>
						<p hidden={this.state.list_set}>Please add at least 2 stops.</p>
            <br />
          </form>
          <ol>{items}</ol>
					<button hidden={!this.state.list_set} type="submit" id="submit_to_run">Optimize Route for {this.state.choice}</button>
	      </div>
	    );
	  }

}
export default List;
