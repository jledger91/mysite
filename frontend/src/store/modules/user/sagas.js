import { all } from 'redux-saga/effects';

import { getUserSaga } from './sagas/getUser';
import { loginSaga } from './sagas/login';
import { logoutSaga } from './sagas/logout';

export default function* combinedSagas() {
  yield all([
    getUserSaga(),
    loginSaga(),
    logoutSaga(),
  ]);
}
