import React, { useEffect, useState } from "react";

import Button from "@mui/joy/Button";
import Input from "@mui/joy/Input";
import Checkbox from "@mui/joy/Checkbox";
import Box from "@mui/joy/Box";

import ReactLoading from "react-loading";
import Autocomplete from "react-google-autocomplete";

const MIN_STOPS = 4;
const MAX_STOPS = 7;

export default function InputGroup() {
  const [inputCount, setInputCount] = useState(4);
  const [result, setResult] = useState<string[]>([]);
  const [inputValues, setInputValues] = useState<string[]>([]);
  const [directionsURL, setDirectionsURL] = useState<string>("");
  const [computedTime, setComputedTime] = useState<number>(0);
  const [submitted, setSubmitted] = useState<boolean>(false);
  const [status, setStatus] = useState<string>("");
  const [checked, setChecked] = useState<boolean>(false);

  const handleAdd = (): void => {
    if (inputCount === MAX_STOPS) {
      return;
    }
    setInputCount(inputCount + 1);
    console.log(inputCount);
  };

  const handleRemove = (): void => {
    if (inputCount === MIN_STOPS) {
      return;
    }
    setInputCount(inputCount - 1);
    console.log(inputCount);
  };

  const handleSubmit = (): void => {
    setSubmitted(true);
    setInputValues(inputValues);
    setResult([]);
    fetch("/get_optimal_route", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        inputValues,
        checked,
      }),
    })
      .then((response) => {
        response.json().then((data) => {
          console.log(data);
          setResult(data.path.map((value: string) => value));
          setDirectionsURL(data.url);
          setComputedTime(data.computation_time);
          setStatus(data.message);
          setSubmitted(false);
        });
      })
      .catch((error) => {
        console.log(error);
      });
  };

  useEffect(() => {
    if (inputCount > inputValues.length) {
      setInputValues([...inputValues, ""]);
    }
  }, [inputCount]);

  const handleChangeInput = (
    e: React.ChangeEvent<HTMLInputElement>,
    index: number
  ): void => {
    const newInputValues = [...inputValues];
    newInputValues[index] = e.target.value;
    setInputValues(newInputValues);
  };

  const allInputsFilled =
    inputValues.length === inputCount &&
    inputCount > 3 &&
    inputValues.every((value) => value !== "");

  return (
    <>
      <Box
        display="flex"
        flexDirection="row"
        justifyContent="center"
        width="100%"
      >
        <Box display="flex" flexDirection="column" width="50%">
          {Array.from({ length: inputCount }, (_, index) => {
            let placeholderText = "";
            let isOrigin = false;
            let isIntermediate = false;
            let isDestination = false;

            if (index === 0) {
              placeholderText = "Origin";
              isOrigin = true;
            } else if (index === inputCount - 1) {
              placeholderText = "Destination";
              isDestination = true;
            } else {
              placeholderText = "Intermediate Stop";
              isIntermediate = true;
            }

            return (
              <Input
                key={index}
                placeholder={placeholderText}
                value={inputValues[index]}
                onChange={(e) => handleChangeInput(e, index)}
              />
            );
          })}
          <Box display="flex" flexDirection="row">
            <Box width="50%">
              {inputCount < MAX_STOPS && (
                <Button onClick={handleAdd}>Add</Button>
              )}
            </Box>
            <Box width="50%">
              {inputCount > MIN_STOPS && (
                <Button onClick={handleRemove}>Remove</Button>
              )}
            </Box>
          </Box>
        </Box>
        <Box display="flex" flexDirection="column" width="50%">
          {inputValues.map((value, index) => {
            if (index === 0) {
              return (
                <p key={index}>
                  Origin: {value}
                  {/* <br /> */}
                </p>
              );
            }
            if (index === inputCount - 1) {
              return (
                <p key={index}>
                  Destination: {value}
                  {/* <br /> */}
                </p>
              );
            }
            return (
              <p key={index}>
                Intermediate Stop: {value}
                {/* <br /> */}
              </p>
            );
          })}
          <Box>
            <Checkbox 
              onChange={() => setChecked(!checked)} />
            Get true optimal route? (May take longer to compute)
          </Box>
          <Button onClick={handleSubmit} disabled={!allInputsFilled}>
            Submit
          </Button>
        </Box>
      </Box>
      <Box>
        {submitted && (
          <ReactLoading
            type={"bars"}
            color={"#abcdef"}
            height={100}
            width={100}
          />
        )}
        {result.length > 0 && (
          <>
            Retrieved result in {computedTime} seconds.
            <ol>
              {result.map((value, index) => {
                return <li key={index}>{value}</li>;
              })}
            </ol>
            <a href={directionsURL} target="_blank" rel="noopener noreferrer">
              See on Google Maps
            </a>
          </>
        )}
        {result.length === 0 && (
          <p>
            {status} <br />
          </p>
        )}
      </Box>
    </>
  );
}
