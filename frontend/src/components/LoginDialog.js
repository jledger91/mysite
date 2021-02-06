import { useState } from 'react';
import { useDispatch } from 'react-redux';

import {
  Button,
  Dialog, DialogActions, DialogContent,
  DialogTitle,
  Divider,
  TextField,
} from '@material-ui/core'

import { LOGIN } from '../store/modules/user/actions';

import './LoginDialog.scss';

const LoginDialog = (props) => {
  
  const { onClose, open } = props;
  
  const dispatch = useDispatch();
  
  const [username, setUsername] = useState(undefined);
  const [password, setPassword] = useState(undefined);
  
  const handleLoginSubmit = () => {
    dispatch({ type: LOGIN, payload: { username, password }});
    onClose();
  }
  const onUsernameChange = (event) => setUsername(event.target.value);
  const onPasswordChange = (event) => setPassword(event.target.value);
  const loginDisabled = !(username && password);
  
  return (
    <Dialog className='login-dialog'
            onClose={onClose}
            open={open}>
      <DialogTitle className='login-title'>
        MySite
      </DialogTitle>
      <Divider/>
      <DialogContent>
        <TextField className='username-field'
                   label='Username'
                   onChange={onUsernameChange}/>
        <TextField className='password-field'
                   label='Password'
                   type='password'
                   onChange={onPasswordChange}/>
      </DialogContent>
      <DialogActions>
        <Button className='login-button'
                color='primary'
                onClick={handleLoginSubmit}
                disabled={loginDisabled}>
          Login
        </Button>
      </DialogActions>
    </Dialog>
  );
}

export default LoginDialog;
