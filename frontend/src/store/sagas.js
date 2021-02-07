import { all } from 'redux-saga/effects';

import authSagas from './modules/auth/sagas';
import filmSagas from './modules/film/sagas';
import reviewSagas from './modules/review/sagas';
import userSagas from './modules/user/sagas';

export function* rootSaga() {
  yield all([
    authSagas(),
    filmSagas(),
    reviewSagas(),
    userSagas(),
  ])
}
