import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { CHECK_AUTHENTICATED, GET_USER } from '../actions';

function* checkAuthenticated() {
  const result = yield http.post('/api/is_authenticated/');
  if (result.status === 200) {
    yield put({ type: GET_USER, payload: {
        username: result.json.username,
      }});
  }
}

export function* checkAuthenticatedSaga() {
  yield takeLatest(CHECK_AUTHENTICATED, checkAuthenticated);
}
