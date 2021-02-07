import { useEffect, useState } from 'react';

import {
  Dialog,
  DialogTitle,
  Tab,
  Tabs,
} from '@material-ui/core';

import LoginForm from './LoginForm';
import RegisterForm from './RegisterForm';

import './LoginDialog.scss';

const LoginDialog = (props) => {
  
  const { onClose, open } = props;
  
  const [showLoginForm, setShowLoginForm] = useState(true);
  
  const handleTabChange = (event, newValue) => {
    setShowLoginForm(!Boolean(newValue));
  }

  useEffect(() => {
    if (open) setShowLoginForm(true);
  }, [open]);
  
  return (
    <Dialog className='login-dialog-component'
            onClose={onClose}
            open={open}>
      <DialogTitle className='tabs-bar'>
        <Tabs onChange={handleTabChange} value={showLoginForm ? 0 : 1}>
          <Tab label='Sign in' disabled={showLoginForm}/>
          <Tab label='Register' disabled={!showLoginForm}/>
        </Tabs>
      </DialogTitle>
      {
        showLoginForm ?
          <LoginForm onClose={onClose} />
          :
          <RegisterForm onClose={onClose} />
      }
    </Dialog>
  );
}

export default LoginDialog;
