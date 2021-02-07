import { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { useParams } from 'react-router';

import { GET_FILM } from '../../store/modules/film/actions';

import './FilmDetail.scss';

const FilmDetail = () => {

  const dispatch = useDispatch();
  const { id } = useParams();

  useEffect(() => {
    dispatch({ type: GET_FILM, payload: { id } });
  }, [id, dispatch]);
  
  return (
    <div className='film-detail-view'>
    
    </div>
  );
}

export default FilmDetail;
