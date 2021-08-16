import { all } from 'redux-saga/effects';

import { getGoogleClientIdSaga } from './_sagas/getGoogleClientId';

export default function* combinedSagas() {
  yield all([
    getGoogleClientIdSaga(),
  ]);
}
