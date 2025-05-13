import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { IS_AUTHENTICATED, LOGGED_IN } from '../actions';

function* isAuthenticated() {
  const result = yield http.post('/api/auth/is_authenticated/');
  
  const { user } = result.json;
  
  if (result.status === 200 && user) {
    yield put({ type: LOGGED_IN, payload: user });
  }
}

export function* isAuthenticatedSaga() {
  yield takeLatest(IS_AUTHENTICATED, isAuthenticated);
}
