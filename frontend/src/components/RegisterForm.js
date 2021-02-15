import { useState } from 'react';
import { useDispatch } from 'react-redux';

import {
  Button,
  DialogActions,
  DialogContent,
  TextField,
} from '@material-ui/core';

import { REGISTER } from '../store/modules/auth/actions';

import './RegisterForm.scss';

const RegisterForm = (props) => {
  
  const { onClose } = props;
  
  const dispatch = useDispatch();
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
  
  const handleSubmit = (data) => () => {
    dispatch({ type: REGISTER, payload: { data }});
    onClose();
  }
  const handleFormChange = (key) => (event) => setRegisterFormData({
    ...registerFormData,
    [key]: event.target.value || undefined,
  });
  
  return (
    <div className='register-form'>
      <DialogContent>
        {
          fields.map(field =>
            <TextField className='form-field'
                       label={field.label}
                       required={field.required}
                       color='secondary'
                       type={field.type}
                       onChange={handleFormChange(field.name)}/>
          )
        }
      </DialogContent>
      <DialogActions className='action-area'>
        <Button className='register-button'
                onClick={handleSubmit(registerFormData)}
                disabled={registerDisabled}>
          Register
        </Button>
      </DialogActions>
    </div>
  );
}

export default RegisterForm;
