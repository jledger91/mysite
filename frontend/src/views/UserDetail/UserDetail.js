import { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { useParams } from 'react-router';

import { GET_USER } from '../../store/modules/user/actions'

import './UserDetail.scss';

const UserDetail = () => {
  
  const dispatch = useDispatch();
  const { id } = useParams();
  
  useEffect(() => {
    dispatch({ type: GET_USER, payload: { id } })
  }, [id, dispatch])
  
  return (
    <div className='user-detail-view'>
    
    </div>
  );
}

export default UserDetail;
