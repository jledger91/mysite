import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import {
  Button,
  List,
  Typography,
} from '@material-ui/core';
import KeyboardArrowLeftIcon from '@material-ui/icons/KeyboardArrowLeft';
import KeyboardArrowRightIcon from '@material-ui/icons/KeyboardArrowRight';

import { GET_FILMS } from '../store/modules/film/actions';
import FilmCard from './FilmCard';

import './FilmRow.scss';

const FilmRow = (props) => {
  
  const { params, title, value } = props;
  
  const dispatch = useDispatch();
  
  const films = useSelector(state => state.film.list?.[value]);
  
  const onPageTurn = (direction) => () => {
    dispatch({ type: GET_FILMS, payload: {
        key: value,
        params: {
          ...params,
          limit: 4,
          offset: films.pagination.offset + (direction * films.pagination.limit)
        }
      }});
  }
  const previousButtonDisabled = !films?.pagination?.previous;
  const nextButtonDisabled = !films?.pagination?.next;
  
  useEffect(() => {
    dispatch({ type: GET_FILMS, payload: {
        key: value,
        params: {
          ...params,
          limit: 4,
          offset: 0,
        },
      }});
  }, [dispatch, params])
  
  return (
    <div className='film-row-component'>
      <Typography className='list-title'
                  variant='h5'>
        {title}
      </Typography>
      <div className='film-row-container'>
        <Button onClick={onPageTurn(-1)}
                disabled={previousButtonDisabled}>
          <KeyboardArrowLeftIcon/>
        </Button>
        <List className='film-row'>
          {
            films?.results?.map(film => <FilmCard film={film} />)
          }
        </List>
        <Button onClick={onPageTurn(1)}
                disabled={nextButtonDisabled}>
          <KeyboardArrowRightIcon/>
        </Button>
      </div>
    </div>
  );
}

export default FilmRow;
