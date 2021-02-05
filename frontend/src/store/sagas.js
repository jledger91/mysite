import { all } from 'redux-saga/effects';

import userSagas from './modules/user/sagas';

export function* rootSaga() {
  yield all([
    userSagas(),
  ])
}
