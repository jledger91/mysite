import { connectRouter } from 'connected-react-router';

import { combineReducers } from 'redux';

import userReducer from './modules/user/reducer';

export const createRootReducer = (history) => combineReducers({
  user: userReducer,
  router: connectRouter(history),
});
