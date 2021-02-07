import { all } from 'redux-saga/effects';

import { getUserSaga } from './sagas/getUser';
import { getUsersSaga } from './sagas/getUsers';

export default function* combinedSagas() {
  yield all([
    getUserSaga(),
    getUsersSaga(),
  ]);
}
