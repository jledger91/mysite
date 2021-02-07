import { useState } from 'react';
import { useDispatch } from 'react-redux';

import {
  Button,
  Dialog, DialogActions, DialogContent,
  DialogTitle,
  Divider,
  TextField,
} from '@material-ui/core'

import { LOGIN } from '../store/modules/auth/actions';

import './LoginDialog.scss';

const LoginDialog = (props) => {
  
  const { onClose, open } = props;
  
  const dispatch = useDispatch();
  
  const [username, setUsername] = useState(undefined);
  const [password, setPassword] = useState(undefined);
  
  const handleLoginSubmit = () => {
    dispatch({ type: LOGIN, payload: { username, password }});
    handleClose();
  }
  const handleUsernameChange = (event) => setUsername(event.target.value);
  const handlePasswordChange = (event) => setPassword(event.target.value);
  const handleClose = () => {
    setUsername(undefined);
    setPassword(undefined);
    onClose();
  }
  const loginDisabled = !(username && password);
  
  return (
    <Dialog className='login-dialog-component'
            onClose={handleClose}
            open={open}>
      <DialogTitle className='login-title'>
        Sign In
      </DialogTitle>
      <Divider/>
      <DialogContent>
        <TextField className='username-field'
                   label='Username'
                   color='secondary'
                   onChange={handleUsernameChange}/>
        <TextField className='password-field'
                   label='Password'
                   type='password'
                   color='secondary'
                   onChange={handlePasswordChange}/>
      </DialogContent>
      <DialogActions>
        <Button className='login-button'
                onClick={handleLoginSubmit}
                disabled={loginDisabled}>
          Sign in
        </Button>
      </DialogActions>
    </Dialog>
  );
}

export default LoginDialog;
