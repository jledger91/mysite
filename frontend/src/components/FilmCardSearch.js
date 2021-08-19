import { useHistory } from 'react-router';

import {
  Card,
  CardMedia,
  Typography,
} from '@material-ui/core';

import { FILM_DETAIL } from '../routes';

import './FilmCardSearch.scss';

const FilmCardSearch = (props) => {
  
  const { film } = props;
  
  const history = useHistory();
  
  const releaseYear = film.releaseDate.slice(0, 4);
  const averageScore = film.averageScore?.toFixed(1) || '--';
  
  const handleOnClick = () => {
    history.push(FILM_DETAIL.replace(':id', film.id))
  }
  
  return (
    <div className='film-card-search-component'>
      <Card className='film-card-search'
            onClick={handleOnClick}>
        <CardMedia className='poster'
                   image={film.poster} />
        <div className='film-detail'>
          <div className='title-container'>
            <Typography className='title'
                        variant='h5'>
              {film.title} ({releaseYear})
            </Typography>
            <Typography className='rating'
                        variant='h5'>
              ★ {averageScore}
            </Typography>
          </div>
          <div className='synopsis-container'>
            {film.synopsis}
          </div>
        </div>
      </Card>
    </div>
  );
}

export default FilmCardSearch;
