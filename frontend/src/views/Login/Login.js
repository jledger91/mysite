import './Login.scss';

import {
  useCallback,
  useEffect,
  useState,
} from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router';

import GoogleButton from 'react-google-button';

import { TextField } from '@material-ui/core';

import LoginCard from '../../components/LoginCard';
import { HOME, REGISTER } from '../../routes';
import { LOGIN } from '../../store/modules/auth/actions';

const Login = () => {
  
  const dispatch = useDispatch();
  const history = useHistory();
  const currentUser = useSelector(state => state.auth.username);
  const { googleClientId } = useSelector(state => state.config);
  const [username, setUsername] = useState(undefined);
  const [password, setPassword] = useState(undefined);
  
  const onGoogleLogin = useCallback(() => {
    const googleAuthUrl = `${window.location.origin}/oauth/login/google-oauth2/`;
    const redirectUri = `${window.location.origin}/oauth/complete/google-oauth2/`;
    
    const urlParams = new URLSearchParams({
      response_type: 'code',
      client_id: googleClientId,
      redirect_uri: redirectUri,
    }).toString();
    
    window.location = `${googleAuthUrl}?${urlParams}`;
  }, [googleClientId]);
  
  const loginDisabled = !(username && password);
  
  const handleUsernameChange = (event) => setUsername(event.target.value);
  const handlePasswordChange = (event) => setPassword(event.target.value);
  const handleSubmit = () => {
    dispatch({ type: LOGIN, payload: { username, password }});
  }
  const handleTabChange = () => history.push(REGISTER);
  
  useEffect(() => {
    currentUser && history.push(HOME);
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
  
      {googleClientId && (
        <div className='google'>
          <GoogleButton onClick={onGoogleLogin} />
        </div>
      )}
    </div>
  );
}

export default Login;
