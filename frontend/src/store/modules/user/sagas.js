import { all } from 'redux-saga/effects';

import { loginSaga } from './sagas/login';
import { logoutSaga } from './sagas/logout';

export default function* combinedSagas() {
  yield all([
    loginSaga(),
    logoutSaga(),
  ]);
}
