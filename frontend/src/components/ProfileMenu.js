import { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import {
  IconButton,
  MenuItem,
  Menu,
  Typography,
} from '@material-ui/core';
import { AccountCircle } from '@material-ui/icons';

import { LOGOUT } from '../store/modules/user/actions';

import './ProfileMenu.scss';

const ProfileMenu = () => {
  
  const { user } = useSelector(state => state);
  const [anchorEl, setAnchorEl] = useState(null);
  const dispatch = useDispatch();
  const open = Boolean(anchorEl)
  
  const handleToggle = (event) => setAnchorEl(event.currentTarget);
  
  const handleLogout = () => {
    dispatch({ type: LOGOUT });
    handleClose();
  }
  
  const handleClose = () => setAnchorEl(null);
  
  return (
    <div className='profile-menu-component'>
      <Typography className='username-label'>
        { user?.username }
      </Typography>
      <IconButton className='profile-icon'
                  aria-controls='fade-menu'
                  aria-haspopup='true'
                  onClick={handleToggle}
                  color='inherit'>
        <AccountCircle />
      </IconButton>
      <Menu id="fade-menu"
            anchorEl={anchorEl}
            keepMounted
            open={open}
            onClose={handleClose}>
        <MenuItem onClick={handleClose}>Profile</MenuItem>
        <MenuItem onClick={handleClose}>My account</MenuItem>
        <MenuItem onClick={handleLogout}>Logout</MenuItem>
      </Menu>
    </div>
  );
}

export default ProfileMenu;