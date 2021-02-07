import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { IS_AUTHENTICATED, LOGGED_IN } from '../actions';

function* isAuthenticated() {
  const result = yield http.post('/api/is_authenticated/');
  
  if (result.status === 200) {
    yield put({ type: LOGGED_IN, payload: result.json });
  }
}

export function* isAuthenticatedSaga() {
  yield takeLatest(IS_AUTHENTICATED, isAuthenticated);
}
