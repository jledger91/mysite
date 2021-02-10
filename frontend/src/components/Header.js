import { useState } from 'react';
import { useSelector } from 'react-redux';
import { useHistory } from 'react-router';

import {
  AppBar,
  Button,
  IconButton,
  Toolbar,
} from '@material-ui/core';
import MenuIcon from '@material-ui/icons/Menu';

import { HOME } from '../routes';
import Drawer from './Drawer';
import LoginDialog from './LoginDialog';
import ProfileMenu from './ProfileMenu';

import './Header.scss';

const Header = () => {
  
  const { auth } = useSelector(state => state);
  
  const history = useHistory();
  
  const [loginDialogOpen, setLoginDialogOpen] = useState(false);
  const [drawerOpen, setDrawerOpen] = useState(false);
  
  const handleLoginClick = () => setLoginDialogOpen(true);
  const handleLoginDialogOnClose = () => setLoginDialogOpen(false);
  const handleDrawerClick = () => setDrawerOpen(true);
  const handleDrawerOnClose = () => setDrawerOpen(false);
  const handleHomeClick = () => history.push(HOME);
  
  return (
    <div className='header-component'>
      <AppBar className='app-bar'
              position='static'>
        <Toolbar>
          <div className='header-main'>
            <IconButton color='inherit'
                        onClick={handleDrawerClick}>
              <MenuIcon/>
            </IconButton>
            <Button color='inherit'
                    onClick={handleHomeClick}>
              My Site
            </Button>
          </div>
          <div className='header-auth'>
            {
              auth?.username ?
                <ProfileMenu/>
                :
                <Button color='inherit'
                        onClick={handleLoginClick}>
                  Sign In
                </Button>
            }
          </div>
        </Toolbar>
      </AppBar>
      <LoginDialog open={loginDialogOpen}
                   onClose={handleLoginDialogOnClose}/>
      <Drawer open={drawerOpen}
              onClose={handleDrawerOnClose}/>
    </div>
  );
}

export default Header;
