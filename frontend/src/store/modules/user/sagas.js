import { all } from 'redux-saga/effects';

import { getUserSaga } from './_sagas/getUser';
import { getUsersSaga } from './_sagas/getUsers';

export default function* combinedSagas() {
  yield all([
    getUserSaga(),
    getUsersSaga(),
  ]);
}
