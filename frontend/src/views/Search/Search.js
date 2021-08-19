import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { Typography } from '@material-ui/core';

import { CLEAR_FILMS, GET_FILMS } from '../../store/modules/film/actions';
import { useSearchParams } from '../../utils/url';

import FilmCardSearch from '../../components/FilmCardSearch';

import './Search.scss';

const Search = () => {
  
  const dispatch = useDispatch();
  const { query } = useSearchParams();
  const { results } = useSelector(state => state.film?.list?.search || {});
  
  useEffect(() => {
    query && dispatch({ type: GET_FILMS, payload: {
      key: 'search',
      params: { 'title': query },
    }});
    return () => dispatch({ type: CLEAR_FILMS, payload: 'search' });
  }, [dispatch, query]);
  
  return (
    <div className='search'>
      {results?.length ? (
        <div className='results-list'>
          {results.map(result => (
            <FilmCardSearch key={result.id} film={result} />
          ))}
        </div>
      ) : (
        <div className='no-results'>
          <Typography variant='h5'>
            No results.
          </Typography>
        </div>
      )}
    </div>
  );
}

export default Search;
