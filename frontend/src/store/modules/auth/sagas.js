import { all } from 'redux-saga/effects';

import { isAuthenticatedSaga } from './sagas/isAuthenticated';
import { loginSaga } from './sagas/login';
import { logoutSaga } from './sagas/logout';

export default function* combinedSagas() {
  yield all([
    isAuthenticatedSaga(),
    loginSaga(),
    logoutSaga(),
  ]);
}
