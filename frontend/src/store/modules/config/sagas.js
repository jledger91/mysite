import { all } from 'redux-saga/effects';

import { getConfigSaga } from './_sagas/getConfig';

export default function* combinedSagas() {
  yield all([
    getConfigSaga(),
  ]);
}
