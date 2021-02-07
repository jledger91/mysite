import { useEffect } from 'react';
import { useDispatch } from 'react-redux';

import { GET_REVIEWS } from '../../store/modules/review/actions';

import './ReviewList.scss';

const ReviewList = () => {
  
  const dispatch = useDispatch();
  
  useEffect(() => {
    dispatch({ type: GET_REVIEWS });
  }, [dispatch]);
  
  return (
    <div className='review-list-view'>
    
    </div>
  );
}

export default ReviewList;
