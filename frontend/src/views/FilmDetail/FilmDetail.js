import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router';

import {
  Card,
  CardMedia,
  Typography,
} from '@material-ui/core';

import ReviewListWidget from '../../components/ReviewListWidget';
import { CLEAR_FILM, GET_FILM } from '../../store/modules/film/actions';

import './FilmDetail.scss';

const FilmDetail = () => {
  
  const dispatch = useDispatch();
  const { id } = useParams();
  const film = useSelector(state => state.film?.detail)
  
  const releaseYear = film?.releaseDate.slice(0, 4);
  const averageScore = film?.averageScore?.toFixed(1) || '--';
  const params = {
    'film': film?.id,
    'limit': 5,
  }
  
  useEffect(() => {
    dispatch({ type: GET_FILM, payload: { id } });
    return () => dispatch({ type: CLEAR_FILM });
  }, [id, dispatch]);
  
  return (
    <div className='film-detail-view'>
      <div className='film-details-container'>
        <Card className='film-card'>
          <CardMedia className='poster'
                     image={film?.poster} />
        </Card>
        <div className='film-details'>
          <Typography variant='h4'>
            {film?.title} ({releaseYear})
          </Typography>
          <Typography variant='h5'>
            {film?.rating} | {film?.duration} | {film?.releaseDate} | ★ {averageScore}
          </Typography>
          {film?.synopsis}
        </div>
      </div>
      <div className='review-list-container'>
        {
          film && <ReviewListWidget params={params} />
        }
      </div>
    </div>
  );
}

export default FilmDetail;
