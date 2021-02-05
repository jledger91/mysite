import { all } from 'redux-saga/effects';

import { loginSaga } from './sagas/login';

export default function* combinedSagas() {
  yield all([
    loginSaga(),
  ]);
}
