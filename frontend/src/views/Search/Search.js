import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { CLEAR_FILMS, GET_FILMS } from '../../store/modules/film/actions';
import { useSearchParams } from '../../utils/url';

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
            // TODO: Make a film search card component.
            <div key={result.id}>
              {result.title}
            </div>
          ))}
        </div>
      ) : (
        <div className='no-results'>
          No results.
        </div>
      )}
    </div>
  );
}

export default Search;
