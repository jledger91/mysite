import {
  Button,
  Card,
  DialogActions,
  DialogContent,
  DialogTitle,
  Tab,
  Tabs,
} from '@material-ui/core';

import './LoginCard.scss';

const LoginCard = ({children, ...props}) => {
  
  const {
    handleSubmit,
    handleTabChange,
    submitDisabled,
    submitLabel,
    tab,
  } = props;
  
  return (
    <Card className='login-card-component'>
      <DialogTitle className='tabs-bar'>
        <Tabs onChange={handleTabChange} value={tab}>
          <Tab label='Sign in' disabled={tab === 0}/>
          <Tab label='Register' disabled={tab === 1}/>
        </Tabs>
      </DialogTitle>
      <DialogContent className='form'>
        {children}
      </DialogContent>
      <DialogActions className='action-area'>
        <Button className='action-button'
                onClick={handleSubmit}
                disabled={submitDisabled}>
          {submitLabel}
        </Button>
      </DialogActions>
    </Card>
  );
}

export default LoginCard;
