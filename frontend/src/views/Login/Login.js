import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router';

import { TextField } from '@material-ui/core';

import LoginCard from '../../components/LoginCard';
import { HOME, REGISTER } from '../../routes';
import { LOGIN } from '../../store/modules/auth/actions';

import './Login.scss';

const Login = () => {
  
  const dispatch = useDispatch();
  const history = useHistory();
  const currentUser = useSelector(state => state.auth.username);
  const [username, setUsername] = useState(undefined);
  const [password, setPassword] = useState(undefined);
  
  const loginDisabled = !(username && password);
  
  const handleUsernameChange = (event) => setUsername(event.target.value);
  const handlePasswordChange = (event) => setPassword(event.target.value);
  const handleSubmit = () => {
    dispatch({ type: LOGIN, payload: { username, password }});
  }
  const handleTabChange = () => history.push(REGISTER);
  
  useEffect(() => {
    if (currentUser) {
      history.push(HOME);
    }
  }, [currentUser, history]);
  
  return (
    <div className='login-page'>
      <LoginCard tab={0}
                 handleTabChange={handleTabChange}
                 handleSubmit={handleSubmit}
                 submitDisabled={loginDisabled}
                 submitLabel='Sign in'>
          <TextField className='form-field'
                     label='Username'
                     color='secondary'
                     onChange={handleUsernameChange}/>
          <TextField className='form-field'
                     label='Password'
                     type='password'
                     color='secondary'
                     onChange={handlePasswordChange}/>
      </LoginCard>
    </div>
  );
}

export default Login;
