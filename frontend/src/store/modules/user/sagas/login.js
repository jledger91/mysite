import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { LOGIN, GET_USER } from '../actions';

function* login(action) {
  const result = yield http.post('/api/login/', {
    username: action.payload.username,
    password: action.payload.password,
  });
  
  if (result.status === 200) {
    yield put({ type: GET_USER, payload: {
        username: action.payload.username,
      }});
  }
}

export function* loginSaga() {
  yield takeLatest(LOGIN, login);
}
