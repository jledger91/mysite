import { useHistory } from 'react-router';

import {
  Card,
  CardActionArea,
  CardMedia,
  Typography,
} from '@material-ui/core';

import { FILM_DETAIL } from '../routes';

import './FilmCard.scss';

const FilmCard = (props) => {
  
  const { film } = props;
  
  const history = useHistory();
  
  const handleOnClick = () => {
    history.push(FILM_DETAIL.replace(':id', film.id))
  }
  
  return (
    <div className='film-card-component'>
      <Card className='film-card'>
        <CardActionArea onClick={handleOnClick}>
          <CardMedia className='poster'
                     image={film.poster} />
        </CardActionArea>
      </Card>
      <Typography className='title'
                  variant='h7'>
        {film.title} ({film.release_date.slice(0, 4)})
      </Typography>
    </div>
  );
}

export default FilmCard;
