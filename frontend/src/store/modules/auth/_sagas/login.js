import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { LOGIN, LOGGED_IN } from '../actions';

function* login(action) {
  const result = yield http.post('/api/login/', {
    username: action.payload.username,
    password: action.payload.password,
  });
  
  if (result.status === 200) {
    yield put({ type: LOGGED_IN, payload: result.json.user });
  }
}

export function* loginSaga() {
  yield takeLatest(LOGIN, login);
}
