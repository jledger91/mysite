import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router';

import { CardActionArea, Typography } from '@material-ui/core';

import { REVIEW_DETAIL } from '../routes';
import { CLEAR_REVIEWS, GET_REVIEWS } from '../store/modules/review/actions';

import './ReviewListWidget.scss';

const ReviewListWidget = (props) => {
  
  const { params } = props;
  
  const dispatch = useDispatch();
  const history = useHistory();
  const reviews = useSelector(state => state.review.list)
  
  const fullName = (review) =>
    `${review.userFirstName} ${review.userLastName}`;
  const onReviewClick = (id) => () => {
    history.push(REVIEW_DETAIL.replace(':id', id))
  }
  
  useEffect(() => {
    dispatch({ type: GET_REVIEWS, payload: params });
    return () => dispatch({ type: CLEAR_REVIEWS });
  }, [dispatch, params]);
  
  return (
    <div className='review-list-widget'>
      {
        reviews?.map(review =>
          <div className='review-card'
               key={review.id}>
            <Typography variant='h6'>
              ★ {review.rating} - {fullName(review)} @{review.userUsername}
            </Typography>
            <CardActionArea className='review'
                            onClick={onReviewClick(review.id)}>
              {review.review.slice(0, 750)} ...
            </CardActionArea>
          </div>
        )
      }
    </div>
  );
}

export default ReviewListWidget;
