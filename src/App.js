import React from "react";
import { AppBar, Toolbar, Typography, Container } from "@mui/material";

function App() {
  return (
    <div>
      {/* Top Bar */}
      <AppBar position="static" color="primary">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            CoPirate
          </Typography>
        </Toolbar>
      </AppBar>

      {/* Main Content */}
      <Container sx={{ mt: 4, textAlign: "center" }}>
        <Typography variant="h4" gutterBottom>
          Welcome to CoPirate 
        </Typography>
        <Typography variant="body1">
          Your tagline or description goes here.
        </Typography>
      </Container>
    </div>
  );
}

export default App;

