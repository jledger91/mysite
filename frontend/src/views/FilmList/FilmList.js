import FilmRow from '../../components/FilmRow';

import './FilmList.scss';

const FilmList = () => {
  
  const latestParams = {
    'ordering': 'release_date_desc',
  }
  const topParams = {
    'ordering': 'average_score_desc',
  }
  
  return (
    <div className='film-list-view'>
      <div className='page-header'>
      
      </div>
      <div className='latest-films'>
        <FilmRow title='Latest Releases'
                 value='latest'
                 params={latestParams} />
      </div>
      <div className='top-rated'>
        <FilmRow title='Top Rated'
                 value='top'
                 params={topParams} />
      </div>
    </div>
  );
}

export default FilmList;
