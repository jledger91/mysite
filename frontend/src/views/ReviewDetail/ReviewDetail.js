import { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { useParams } from 'react-router';

import { GET_REVIEW } from '../../store/modules/review/actions'

import './ReviewDetail.scss';

const ReviewDetail = () => {
  
  const dispatch = useDispatch();
  const { id } = useParams();
  
  useEffect(() => {
    dispatch({ type: GET_REVIEW, payload: { id } })
  }, [id, dispatch])
  
  return (
    <div className='review-detail-view'>
    
    </div>
  );
}

export default ReviewDetail;
