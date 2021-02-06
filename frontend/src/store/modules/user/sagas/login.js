import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { LOGIN, LOGIN_SUCCESS } from '../actions';

function* login(action) {
  const result = yield http.post('/api/login/', {
    username: action.payload.username,
    password: action.payload.password,
  });
  
  const { status, json } = result;
  
  if (status === 200) {
    yield put({ type: LOGIN_SUCCESS, payload: {
        firstName: json.firstName,
        lastName: json.lastName,
        username: json.username,
      }});
  }
}

export function* loginSaga() {
  yield takeLatest(LOGIN, login)
}
