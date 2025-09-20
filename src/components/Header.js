import { AppBar, Toolbar, Typography, Container,Avatar } from "@mui/material";

function Header() {
  return (
        <div>
      <AppBar position="static" sx={{ bgcolor: 'white' }}>
        <Toolbar>
          <Avatar alt="CoPirate Logo" src="/CoPirate_logo.png" sx={{ mr: 2, bgcolor: 'grey' }} />
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 , color: '#333',fontFamily:"Lato", fontWeight: 'bold'}}>
            CoPirate
          </Typography>
        </Toolbar>
      </AppBar>

      <Container sx={{ mt: 4, textAlign: "center" }}>
        <Typography variant="h4" gutterBottom sx={{ color: '#333' }}> 
          Welcome to CoPirate 
        </Typography>
        <Typography variant="body1">
          Your tagline or description goes here.
        </Typography>
      </Container>
    </div>

  );
}

export default Header;
