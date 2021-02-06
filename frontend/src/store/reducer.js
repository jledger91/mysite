import { connectRouter } from 'connected-react-router';

import { combineReducers } from 'redux';

import userReducer from './modules/user/reducer';
import filmReducer from './modules/film/reducer';
import reviewReducer from './modules/review/reducer';

export const createRootReducer = (history) => combineReducers({
  user: userReducer,
  film: filmReducer,
  review: reviewReducer,
  router: connectRouter(history),
});
