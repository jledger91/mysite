import { useState } from 'react';
import { useDispatch } from 'react-redux';

import { LOGIN } from '../../store/modules/user/actions';

import './Login.css';

const Login = () => {
  
  const dispatch = useDispatch();
  
  const [ username, setUsername ] = useState(undefined);
  const [ password, setPassword ] = useState(undefined);
  
  const handleLoginSubmit = () => {
    dispatch({ type: LOGIN, payload: { username, password }});
  }
  const onUsernameChange = (event) => setUsername(event.target.value);
  const onPasswordChange = (event) => setPassword(event.target.value);

  return (
    <div>
      <input type='text' onChange={onUsernameChange}/>
      <input type='password' onChange={onPasswordChange}/>
      <button onClick={handleLoginSubmit}> Login </button>
    </div>
  );
}

export default Login;
