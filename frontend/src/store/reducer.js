import { connectRouter } from 'connected-react-router';

import { combineReducers } from 'redux';

import authReducer from './modules/auth/reducer';
import configReducer from './modules/config/reducer';
import filmReducer from './modules/film/reducer';
import reviewReducer from './modules/review/reducer';
import userReducer from './modules/user/reducer';

export const createRootReducer = (history) => combineReducers({
  auth: authReducer,
  config: configReducer,
  film: filmReducer,
  review: reviewReducer,
  user: userReducer,
  router: connectRouter(history),
});
