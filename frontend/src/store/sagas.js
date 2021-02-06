import { all } from 'redux-saga/effects';

import userSagas from './modules/user/sagas';
import filmSagas from './modules/user/sagas';
import reviewSagas from './modules/user/sagas';

export function* rootSaga() {
  yield all([
    userSagas(),
    filmSagas(),
    reviewSagas(),
  ])
}
