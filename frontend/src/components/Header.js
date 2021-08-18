import './Header.scss';

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

import { HOME, LOGIN } from '../routes';
import { useSearchParams } from '../utils/url';
import Drawer from './Drawer';
import ProfileMenu from './ProfileMenu';
import SearchBar from './SearchBar';

const Header = () => {
  
  const history = useHistory();
  const { query } = useSearchParams();
  const { auth } = useSelector(state => state);
  const [drawerOpen, setDrawerOpen] = useState(false);
  
  const handleLoginClick = () => history.push(LOGIN);
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
              MySite
            </Button>
          </div>
          
          <div className='header-search'>
            <SearchBar initialValue={query} />
          </div>
          
          <div className='header-auth'>
            {auth?.username ? (
              <ProfileMenu/>
            ):(
              <Button color='inherit'
                      onClick={handleLoginClick}>
                Sign In
              </Button>
            )}
          </div>
        </Toolbar>
      </AppBar>
      <Drawer open={drawerOpen}
              onClose={handleDrawerOnClose}/>
    </div>
  );
}

export default Header;
