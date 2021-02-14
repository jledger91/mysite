import FilmRow from '../../components/FilmRow';

import './FilmList.scss';

const FilmList = () => {
  
  const categories = [
    {
      key: 'latest',
      title: 'Latest Releases',
      params: {
        'released_after': '2015-01-01',
        'ordering': 'release_date_desc',
      },
    },
    {
      key: 'top',
      title: 'Top Rated',
      params: {
        'min_average_score': 8,
        'ordering': 'average_score_desc',
      },
    },
    {
      key: 'nineties',
      title: '90\'s Films',
      params: {
        'released_after': '1990-01-01',
        'released_before': '2000-01-01',
      },
    },
    {
      key: 'eighties',
      title: '80\'s Films',
      params: {
        'released_after': '1980-01-01',
        'released_before': '1990-01-01',
      },
    },
    {
      key: 'all',
      title: 'All',
      params: {
        'ordering': 'title_asc',
      },
    },
  ]
  
  return (
    <div className='film-list-view'>
      <div className='page-header'>
      
      </div>
      {
        categories.map(category =>
          <div className={category.key} key={category.key}>
            <FilmRow title={category.title}
                     value={category.key}
                     params={category.params} />
          </div>
        )
      }
    </div>
  );
}

export default FilmList;
