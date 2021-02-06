import { takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { LOGOUT } from '../actions';

function* logout(action) {
  const result = yield http.post('/api/logout/', {});
  const { status } = result;
  if (status === 200) {
    // TODO: Toast for successful logout.
  }
}

export function* logoutSaga() {
  yield takeLatest(LOGOUT, logout)
}
