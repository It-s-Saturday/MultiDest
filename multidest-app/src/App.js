import React, { useState } from 'react';
import Container from '@material-ui/core/Container';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import RemoveIcon from '@material-ui/icons/Remove';
import AddIcon from '@material-ui/icons/Add';
import Icon from '@material-ui/core/Icon';
import ExploreIcon from '@material-ui/icons/Explore';
import { v4 as uuidv4 } from 'uuid';

import { makeStyles } from '@material-ui/core/styles';

// Adapted from https://github.com/candraKriswinarto/dymanic-form

const useStyles = makeStyles((theme) => ({
  root: {
    '& .MuiTextField-root': {
      margin: theme.spacing(1),
    },
  },
  button: {
    margin: theme.spacing(1),
    width: '100px'
  }
}))


function App() {
  var list = [];
  const classes = useStyles()
  const [inputFields, setInputFields] = useState([
    { id: uuidv4(), stop: ''},
  ]);


  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("InputFields", inputFields);
  };

  const handleChangeInput = (id, event) => {
    const newInputFields = inputFields.map(i => {
      if(id === i.id) {
        i[event.target.name] = event.target.value
      }
      return i;
    })

    setInputFields(newInputFields);
  }

  const handleRadio = () => {

  }
  const handleRadio2 = () => {

  }

  let parseInput = (event) => {
    console.log("Parse clicked.");
    var parsed = "";
    parsed = inputFields;
    var stops = "";
    for (var i = 0; i < parsed.length; i++) {
      // console.log(parsed[i]['stop']);
      let t = i;
                if (t === 0) {
                    t = "Origin";
                }
                else if (t === parsed.length-1) {
                    t = "Destination";
                }
                else {
                    t = "Stop " + i;
                    stops += t + ": " + parsed[i]['stop'] + "\n";
                }
                parsed[i]['stop'] = t + ": " + parsed[i]['stop'];
                console.log(parsed[i]['stop']);
    }
    try {
    alert(parsed[0]['stop'] + "\n" + stops + parsed[parsed.length-1]['stop']);
    }
    catch(e) { console.error(e); }
}

  const handleAddFields = id => {
    let values = [...inputFields];
    let temp = values.findIndex(value => value.id === id) + 1;
    // console.log(temp)
    values.splice(temp, 0, {id: uuidv4(), stop: ''});
    setInputFields(values);
  }

  const handleRemoveFields = id => {
    const values  = [...inputFields];
    values.splice(values.findIndex(value => value.id === id), 1);
    setInputFields(values);
  }


  return (
    <Container>
    <h1>Start App.js</h1>
      <form className={classes.root} method="GET" action="/parse_function">
      <div>
      <div>
        <input onChange={handleRadio()} type ="radio" id="distance" name="optimize_for" value="distance" />
        <label for="distance_choice">distance</label>
        <input onChange={handleRadio()} type ="radio" id="timeout" name="optimize_for" value="time" />
        <label for="time_choice">time</label>
      </div>
      <div>
          <input onChange={handleRadio2()} type="radio" id="driving" name="method" value="driving" />
          <label for="driving-choice">driving</label>
          <input onChange={handleRadio2()} type="radio" id="walking" name="method" value="walking" />
          <label for="walking-choice">walking</label>
          <input onChange={handleRadio2()} type="radio" id="biking" name="method" value="biking" />
          <label for="biking-choice">biking</label>


      </div>
      </div>
        { inputFields.map(inputField => (
          <div>
          <div key={inputField.id}>
            <TextField
              name="stop"
              label="Stop"
              variant="filled"
              value={inputField.firstName}
              onChange={event => handleChangeInput(inputField.id, event)}
              required
            />
            <IconButton disabled={inputFields.length <= 4} onClick={() => handleRemoveFields(inputField.id)}>
              <RemoveIcon />
            </IconButton>
            <IconButton
              onClick={() => handleAddFields(inputField.id)}
            >
              <AddIcon />
            </IconButton>
          </div>
          </div>
        )) }

        <Button
          className={classes.button}
          variant="contained"
          onClick={() => parseInput()}
        >Parse
        </Button>
        <button className={classes.button} disabled={inputFields.length < 4} type="submit" id="submit_to_run">travel</button>
      </form>
    </Container>
  );
}


export default App;
