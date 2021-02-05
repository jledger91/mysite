import { routerMiddleware } from 'connected-react-router';

import { createBrowserHistory } from 'history';

import { applyMiddleware, createStore } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import createSagaMiddleware from 'redux-saga';

import { createRootReducer } from './reducer';
import { rootSaga } from './sagas';

export const history = createBrowserHistory();
const rootReducer = createRootReducer(history);
const sagaMiddleware = createSagaMiddleware();

export const store = createStore(
  rootReducer,
  composeWithDevTools(applyMiddleware(
    routerMiddleware(history),
    sagaMiddleware,
  ))
)

sagaMiddleware.run(rootSaga);
