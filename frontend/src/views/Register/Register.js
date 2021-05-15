import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router';

import { TextField } from '@material-ui/core';

import LoginCard from '../../components/LoginCard';
import { HOME, LOGIN } from '../../routes';
import { REGISTER } from '../../store/modules/auth/actions';

import './Register.scss';

const Register = () => {
  
  const dispatch = useDispatch();
  const history = useHistory();
  const currentUser = useSelector(state => state.auth.username);
  const [registerFormData, setRegisterFormData] = useState({});
  
  const fields = [
    {
      name: 'username',
      label: 'Username',
      required: true,
    },
    {
      name: 'first_name',
      label: 'First Name',
    },
    {
      name: 'last_name',
      label: 'Last Name',
    },
    {
      name: 'email',
      label: 'Email',
    },
    {
      name: 'password',
      label: 'Password',
      type: 'password',
      required: true,
    }
  ];
  const registerDisabled = fields
    .filter(field => field.required)
    .reduce((acc, cur) =>
      !registerFormData[cur.name] ? true : acc, false);
  
  const handleSubmit = () => {
    dispatch({ type: REGISTER, payload: { data: registerFormData }});
  }
  const handleFormChange = (key) => (event) => setRegisterFormData({
    ...registerFormData,
    [key]: event.target.value || undefined,
  });
  const handleTabChange = () => history.push(LOGIN);
  
  useEffect(() => {
    if (currentUser) {
      history.push(HOME);
    }
  }, [currentUser, history]);
  
  return (
    <div className='register-page'>
      <LoginCard tab={1}
                 handleTabChange={handleTabChange}
                 handleSubmit={handleSubmit}
                 submitDisabled={registerDisabled}
                 submitLabel='Register'>
        {
          fields.map(field =>
            <TextField className='form-field'
                       key={field.name}
                       label={field.label}
                       required={field.required}
                       color='secondary'
                       type={field.type}
                       onChange={handleFormChange(field.name)}/>
          )
        }
      </LoginCard>
    </div>
  );
}

export default Register;
