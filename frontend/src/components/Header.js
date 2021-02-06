import { useState } from 'react';
import { useSelector } from 'react-redux';

import {
  AppBar,
  Button,
  Toolbar,
  Typography,
} from '@material-ui/core';

import LoginDialog from './LoginDialog';
import ProfileMenu from "./ProfileMenu";

import './Header.scss';

const Header = () => {
  
  const { user } = useSelector(state => state);
  
  const [loginDialogOpen, setLoginDialogOpen] = useState(false);
  
  const handleLoginClick = () => setLoginDialogOpen(true);
  const handleLoginDialogOnClose = () => setLoginDialogOpen(false);
  
  return (
    <div className='header'>
      <AppBar position='static'
              className='app-bar'>
        <Toolbar>
          <Typography className='title'
                      variant='h6'>
            My Site
          </Typography>
          {
            user?.username ?
              <ProfileMenu/>
              :
              <Button color='inherit'
                      onClick={handleLoginClick}>
                Sign In
              </Button>
          }
        </Toolbar>
      </AppBar>
      <LoginDialog open={loginDialogOpen}
                   onClose={handleLoginDialogOnClose}/>
    </div>
  );
}

export default Header;
