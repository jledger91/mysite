import { ConnectedRouter } from 'connected-react-router';

import { Suspense, useEffect } from 'react';
import { Provider } from 'react-redux';
import { Switch } from 'react-router';
import { Route } from 'react-router-dom';

import { CircularProgress } from '@material-ui/core';

import Header from './components/Header';
import * as r from './routes';
import Home from './views/Home/Home';
import FilmDetail from './views/FilmDetail/FilmDetail';
import FilmList from './views/FilmList/FilmList';
import ReviewDetail from './views/ReviewDetail/ReviewDetail';
import ReviewList from './views/ReviewList/ReviewList';
import UserDetail from './views/UserDetail/UserDetail';
import UserList from './views/UserList/UserList';
import { history, store } from './store';
import { IS_AUTHENTICATED } from './store/modules/auth/actions';

import 'antd/dist/antd.css';

import './App.scss';

function App() {
  
  useEffect(() => {
    store.dispatch({ type: IS_AUTHENTICATED });
  }, []);
  
  const Loading = <CircularProgress/>;
  
  const Routes = <Switch>
    <Route exact path={r.HOME} component={Home} />
    <Route exact path={r.FILM_DETAIL} component={FilmDetail} />
    <Route exact path={r.FILM_LIST} component={FilmList} />
    <Route exact path={r.REVIEW_DETAIL} component={ReviewDetail} />
    <Route exact path={r.REVIEW_LIST} component={ReviewList} />
    <Route exact path={r.USER_DETAIL} component={UserDetail} />
    <Route exact path={r.USER_LIST} component={UserList} />
  </Switch>;
  
  return (
    <Suspense fallback={Loading}>
      <Provider store={store}>
        <ConnectedRouter history={history}>
          <Header/>
          <div className='page'>
            <div className='page-content'>
              {Routes}
            </div>
          </div>
        </ConnectedRouter>
      </Provider>
    </Suspense>
  );
}

export default App;
