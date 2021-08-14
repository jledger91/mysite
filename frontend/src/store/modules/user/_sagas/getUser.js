import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { GET_USER, SET_USER } from '../actions';

function* getUser(action) {
  const { id } = action.payload;
  
  const result = yield http.get(`/api/users/${id}`);
  
  if (result.status === 200) {
    yield put({ type: SET_USER, payload: {
        detail: result.json,
      }});
  }
}

export function* getUserSaga() {
  yield takeLatest(GET_USER, getUser);
}
