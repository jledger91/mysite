import { ConnectedRouter } from 'connected-react-router';

import { Suspense } from 'react';
import { Provider } from 'react-redux';
import { Switch } from 'react-router';
import { Route } from 'react-router-dom';

import { CircularProgress } from '@material-ui/core';

import Header from './components/Header';
import Home from './views/Home/Home';
import * as r from './routes';
import { history, store } from './store';

import './App.scss';

function App() {
  
  const Loading = <CircularProgress/>
  
  const routes = (<Switch>
    <Route exact path={r.home} component={Home}/>
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
