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
  
  const {
    pageTurnOffset,
    paginationLimit,
    params,
    title,
    value,
  } = props;
  
  const dispatch = useDispatch();
  const films = useSelector(state => state.film.list?.[value]);
  
  const previousButtonDisabled = !films?.pagination?.previous;
  const nextButtonDisabled = !films?.pagination?.next;
  
  const onPageTurn = (direction) => () => {
    dispatch({ type: GET_FILMS, payload: {
        key: value,
        params: {
          ...params,
          limit: paginationLimit,
          offset: films.pagination.offset + (direction * pageTurnOffset)
        }
      }});
  };
  
  useEffect(() => {
    dispatch({ type: GET_FILMS, payload: {
        key: value,
        params: {
          ...params,
          limit: paginationLimit,
          offset: 0,
        }
      }});
  }, [
    dispatch,
    paginationLimit,
    params,
    value,
  ]);
  
  return (
    <div>
      {
        films &&
        <div className='film-row-component'>
          <Typography className='row-title'
                      variant='h5'>
            {title}
          </Typography>
          <div className='film-row-container'>
            <Button onClick={onPageTurn(-1)}
                    disabled={previousButtonDisabled}>
              <KeyboardArrowLeftIcon/>
            </Button>
            <List className='film-row'>
              {films?.results?.map(film => (
                <FilmCard key={film.id} film={film} />)
              )}
            </List>
            <Button onClick={onPageTurn(1)}
                    disabled={nextButtonDisabled}>
              <KeyboardArrowRightIcon/>
            </Button>
          </div>
        </div>
      }
    </div>
  );
}

export default FilmRow;
