import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { LOGIN, LOGIN_SUCCESS } from '../actions';

function* login(action) {
  // TODO: '/auth/login/' won't work for this purpose, so some backend
  //  work needs to be done, then this URI can be changed.
  const result = yield http.post('/auth/login/', {
    username: action.username,
    password: action.password,
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
