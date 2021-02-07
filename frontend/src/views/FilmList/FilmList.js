import { useEffect } from 'react';
import { useDispatch } from 'react-redux';

import { GET_FILMS } from '../../store/modules/film/actions';

import './FilmList.scss';

const FilmList = () => {
  
  const dispatch = useDispatch();
  
  useEffect(() => {
    dispatch({ type: GET_FILMS });
  }, [dispatch]);
  
  return (
    <div className='film-list-view'>
    
    </div>
  );
}

export default FilmList;
