import React from 'react';


class List extends React.Component {
    constructor(props) {
    super(props);
    // Change code below this line
    this.state = {
        outlist: [],
        userInput: "",
        list: [],
        list_set: false,
        choice: "",
        choice_set: false,
        method: "",
        method_set: false,
				enable_optimize: this.choice_set && this.method_set,
    }
    // Change code above this line
    this.handleRadio = this.handleRadio.bind(this);
    this.handleRadio2 = this.handleRadio2.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.parseInput = this.parseInput.bind(this);
    }

    parseInput() {
        const parsed = this.state.userInput.split('\n').filter(e => e !== "" );
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
                if (t === 0) {
                    t = "Origin";
                }
                else if (t === visual_parsed.length-1) {
                    t = "Destination";
                }
                else {
                    t = "Stop " + i;
                }
                visual_parsed[i] = t + ": " + visual_parsed[i];
            }

            this.setState({
                list: visual_parsed,
                list_set: true,
                outlist: parsed
            });
        }
    }

    handleRadio(e) {
        this.setState({
            choice: e.target.value,
            choice_set: true
        });
    }
    handleRadio2(e) {
        this.setState({
            method: e.target.value,
            method_set: true

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
          <form method="POST" action="/parse_function" >
            <div>
              <input onChange={this.handleRadio} type ="radio" id="distance" name="optimize_for" value="distance" />
              <label for="distance_choice">distance</label>
              <input onChange={this.handleRadio} type ="radio" id="timeout" name="optimize_for" value="time" />
              <label for="time_choice">time</label>
              </div>
                        <div>
                            <input onChange={this.handleRadio2} type="radio" id="driving" name="method" value="driving" />
                            <label for="driving-choice">driving</label>
                            <input onChange={this.handleRadio2} type="radio" id="walking" name="method" value="walking" />
                            <label for="walking-choice">walking</label>
                            <input onChange={this.handleRadio2} type="radio" id="biking" name="method" value="biking" />
                            <label for="biking-choice">biking</label>


                        </div>
            <br/>
                        <br />
            <button onClick={this.parseInput} type="button">Parse route</button>
                        <p hidden={this.state.list_set}>Please add at least 2 stops.</p>
            <br />
                        <ol>{items}</ol>
                        <button hidden={!this.state.list_set} disabled={this.state.enable_optimize} type="submit" id="submit_to_run">Optimize Route for {this.state.choice}</button>
          </form>
          </div>
        );
    }

}
export default List;
