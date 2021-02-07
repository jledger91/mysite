import { useEffect } from 'react';
import { useDispatch } from 'react-redux';

import { GET_USERS } from '../../store/modules/user/actions';

import './UserList.scss';

const UserList = () => {
  
  const dispatch = useDispatch();
  
  useEffect(() => {
    dispatch({ type: GET_USERS });
  }, [dispatch]);
  
  return (
    <div className='user-list-view'>
    
    </div>
  );
}

export default UserList;
