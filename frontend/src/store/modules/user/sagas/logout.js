import { takeLatest } from 'redux-saga/effects';

import { LOGOUT } from '../actions';
import * as http from '../../../../utils/http';

function* logout() {
  const result = yield http.post('/api/logout/');
  if (result.status === 200) {
    // TODO: Toast for successful logout.
  }
}

export function* logoutSaga() {
  yield takeLatest(LOGOUT, logout)
}
