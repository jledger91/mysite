import { put, takeLatest } from 'redux-saga/effects';

import { LOGOUT, LOGGED_OUT } from '../actions';
import * as http from '../../../../utils/http';

function* logout() {
  const result = yield http.post('/api/logout/');
  if (result.status === 200) {
    yield put({ type: LOGGED_OUT })
  }
}

export function* logoutSaga() {
  yield takeLatest(LOGOUT, logout)
}
