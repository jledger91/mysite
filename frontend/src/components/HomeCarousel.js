import { Carousel } from 'antd';

import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router';

import { CardActionArea, CardMedia } from '@material-ui/core';

import { FILM_DETAIL } from '../routes';
import { GET_FILMS } from '../store/modules/film/actions';

import './HomeCarousel.scss';

const HomeCarousel = () => {
  
  const dispatch = useDispatch();
  const history = useHistory();
  
  const films = useSelector(state => state.film.list?.home);
  
  const PAGINATION_LIMIT = 3;
  
  const handleOnClick = (id) => () => {
    history.push(FILM_DETAIL.replace(':id', id))
  }
  
  useEffect(() => {
    dispatch({ type: GET_FILMS, payload: {
        key: 'home_carousel',
        params: {
          ordering: 'release_date_desc',
          limit: PAGINATION_LIMIT,
          offset: 0,
        },
      }});
  }, [dispatch])
  
  return (
    <Carousel className='home-carousel'
              autoplay>
      {
        films?.results?.map(film => <div key={film.id}>
          <CardActionArea onClick={handleOnClick(film.id)}>
            <CardMedia className='poster'
                       image={film.poster} />
          </CardActionArea>
        </div>)
      }
    </Carousel>
  );
}

export default HomeCarousel;
