import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { LOGOUT, LOGGED_OUT } from '../actions';

function* logout() {
  const result = yield http.post('/api/auth/logout/');
  
  if (result.status === 200) {
    yield put({ type: LOGGED_OUT });
  }
}

export function* logoutSaga() {
  yield takeLatest(LOGOUT, logout);
}
