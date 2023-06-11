import React from "react";
import InputGroup from "./components/InputGroup";
import ServerStatus from "./components/ServerStatus";
import { Box } from "@mui/joy";


const App: React.FC = () => {
  return (
    <Box sx={{padding: 2}} mx={{padding: 4}}>
      <InputGroup />
      <ServerStatus />
    </Box>
  );
};

export default App;
