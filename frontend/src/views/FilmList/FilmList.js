import FilmRow from '../../components/FilmRow';

import './FilmList.scss';

const FilmList = () => {
  
  const LATEST_RANGE = 4;
  const PAGE_TURN_OFFSET = 1;
  const PAGINATION_LIMIT = 4;
  
  const currentYear = new Date().getFullYear();
  
  const categories = [
    {
      key: 'latest',
      title: 'Latest Releases',
      params: {
        'released_after': `${currentYear - LATEST_RANGE - 1}-12-31`,
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
        'released_after': '1989-12-31',
        'released_before': '2000-01-01',
      },
    },
    {
      key: 'eighties',
      title: '80\'s Films',
      params: {
        'released_after': '1979-12-31',
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
                     params={category.params}
                     paginationLimit={PAGINATION_LIMIT}
                     pageTurnOffset={PAGE_TURN_OFFSET} />
          </div>
        )
      }
    </div>
  );
}

export default FilmList;
