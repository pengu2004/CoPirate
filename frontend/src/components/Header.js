import {
  AppBar,
  Toolbar,
  Typography,
  Avatar,
  Button,
} from "@mui/material";
function Header() {
  return (
    <div>
      <AppBar position="static" sx={{ bgcolor: "white" }}>
        <Toolbar>
          <Avatar
            alt="CoPirate Logo"
            src="/CoPirate_logo.png"
            sx={{ mr: 2, bgcolor: "white" }}
          />
          <Typography
            variant="h6"
            component="div"
            sx={{
              flexGrow: 1,
              color: "#333",
              fontFamily: "Lato",
              fontWeight: "bold",
            }}
          >
            CoPirate
          </Typography>
          <Button color="secondary" bgcolor="primary">Sign In</Button>
        </Toolbar>
      </AppBar>
    </div>
  );
}

export default Header;
