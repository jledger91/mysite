import { useState } from 'react';
import { useDispatch } from 'react-redux';

import {
  Button,
  DialogActions,
  DialogContent,
  TextField,
} from '@material-ui/core';

import { LOGIN } from '../store/modules/auth/actions';

import './LoginForm.scss';

const LoginForm = (props) => {
  
  const { onClose } = props;
  
  const dispatch = useDispatch();
  
  const [username, setUsername] = useState(undefined);
  const [password, setPassword] = useState(undefined);
  
  const loginDisabled = !(username && password);
  
  const handleUsernameChange = (event) => setUsername(event.target.value);
  const handlePasswordChange = (event) => setPassword(event.target.value);
  const handleSubmit = () => {
    dispatch({ type: LOGIN, payload: { username, password }});
    onClose();
  }

  return (
    <div className='login-form'>
      <DialogContent>
        <TextField className='form-field'
                   label='Username'
                   color='secondary'
                   onChange={handleUsernameChange}/>
        <TextField className='form-field'
                   label='Password'
                   type='password'
                   color='secondary'
                   onChange={handlePasswordChange}/>
      </DialogContent>
      <DialogActions className='action-area'>
        <Button className='login-button'
                onClick={handleSubmit}
                disabled={loginDisabled}>
          Sign In
        </Button>
      </DialogActions>
    </div>
  );
}

export default LoginForm;
