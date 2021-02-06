import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { GET_USER, SET_USER } from '../actions';

function* getUser(action) {
  const result = yield http.get('/api/users/', {
    username: action.payload.username,
  });
  
  const user = result.json[0];
  
  if (result.status === 200) {
    yield put({ type: SET_USER, payload: {
        username: user.username,
        firstName: user.first_name,
        lastName: user.last_name,
      }});
  }
}

export function* getUserSaga() {
  yield takeLatest(GET_USER, getUser)
}
