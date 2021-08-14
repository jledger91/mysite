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
import Login from './views/Login/Login';
import NotFound from './views/404/404';
import Register from './views/Register/Register';
import ReviewDetail from './views/ReviewDetail/ReviewDetail';
import ReviewList from './views/ReviewList/ReviewList';
import UserDetail from './views/UserDetail/UserDetail';
import UserList from './views/UserList/UserList';
import { history, store } from './store';
import { IS_AUTHENTICATED } from './store/modules/auth/actions';

import 'antd/dist/antd.css';
import './App.scss';

const App = () => {
  
  const Loading = <CircularProgress/>;
  const Routes = <Switch>
    <Route exact path={r.HOME} component={Home} />
    <Route exact path={r.FILM_DETAIL} component={FilmDetail} />
    <Route exact path={r.FILM_LIST} component={FilmList} />
    <Route exact path={r.LOGIN} component={Login} />
    <Route exact path={r.REGISTER} component={Register} />
    <Route exact path={r.REVIEW_DETAIL} component={ReviewDetail} />
    <Route exact path={r.REVIEW_LIST} component={ReviewList} />
    <Route exact path={r.USER_DETAIL} component={UserDetail} />
    <Route exact path={r.USER_LIST} component={UserList} />
    {/* 404 */}
    <Route path='*' component={NotFound} />
  </Switch>;
  
  useEffect(() => {
    store.dispatch({ type: IS_AUTHENTICATED });
  }, []);
  
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
