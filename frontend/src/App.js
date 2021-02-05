import { ConnectedRouter } from 'connected-react-router';

import { Suspense } from 'react';
import { Provider } from 'react-redux';
import { Switch } from 'react-router';
import { Route } from 'react-router-dom';

import Login from './views/Login/Login';
import * as r from './routes';
import { history, store } from './store';

import './App.css';

function App() {
  
  const routes = (<Switch>
    <Route exact path={r.login} component={Login}/>
  </Switch>);
  
  return (
    <Suspense fallback={null}>
      <Provider store={store}>
        <ConnectedRouter history={history}>
          {routes}
        </ConnectedRouter>
      </Provider>
    </Suspense>
  );
}

export default App;
