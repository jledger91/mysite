import { ConnectedRouter } from 'connected-react-router';

import { Suspense, useEffect } from 'react';
import { Provider } from 'react-redux';
import { Switch } from 'react-router';
import { Route } from 'react-router-dom';

import { CircularProgress } from '@material-ui/core';

import Header from './components/Header';
import Home from './views/Home/Home';
import FilmDetail from './views/FilmDetail/FilmDetail';
import FilmList from './views/FilmList/FilmList';
import ReviewDetail from './views/ReviewDetail/ReviewDetail';
import ReviewList from './views/ReviewList/ReviewList';
import UserDetail from './views/UserDetail/UserDetail';
import UserList from './views/UserList/UserList';
import * as r from './routes';
import { history, store } from './store';
import { IS_AUTHENTICATED } from './store/modules/auth/actions';

import './App.scss';

function App() {
  
  useEffect(() => {
    store.dispatch({ type: IS_AUTHENTICATED });
  }, []);
  
  const Loading = <CircularProgress/>;
  
  const routes = (<Switch>
    <Route exact path={r.home} component={Home} />
    <Route exact path={r.film} component={FilmDetail} />
    <Route exact path={r.films} component={FilmList} />
    <Route exact path={r.review} component={ReviewDetail} />
    <Route exact path={r.reviews} component={ReviewList} />
    <Route exact path={r.user} component={UserDetail} />
    <Route exact path={r.users} component={UserList} />
  </Switch>);
  
  return (
    <Suspense fallback={Loading}>
      <Provider store={store}>
        <ConnectedRouter history={history}>
          <Header/>
          {routes}
        </ConnectedRouter>
      </Provider>
    </Suspense>
  );
}

export default App;
