import { all } from 'redux-saga/effects';

import { isAuthenticatedSaga } from './_sagas/isAuthenticated';
import { loginSaga } from './_sagas/login';
import { logoutSaga } from './_sagas/logout';
import { registerSaga } from './_sagas/register';

export default function* combinedSagas() {
  yield all([
    isAuthenticatedSaga(),
    loginSaga(),
    logoutSaga(),
    registerSaga(),
  ]);
}
