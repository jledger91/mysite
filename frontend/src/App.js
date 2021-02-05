import { ConnectedRouter } from 'connected-react-router';

import { Suspense } from 'react';
import { Provider } from 'react-redux';

import { history, store } from './store';

import './App.css';

function App() {
  return (
    <Suspense>
      <Provider store={store}>
        <ConnectedRouter history={history}>
        
        </ConnectedRouter>
      </Provider>
    </Suspense>
  );
}

export default App;
