import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { GET_REVIEW, SET_REVIEW } from '../actions';

function* getReview(action) {
  const { id } = action.payload;
  
  const result = yield http.get(`/api/reviews/${id}`);
  
  if (result.status === 200) {
    yield put({ type: SET_REVIEW, payload: {
        detail: result.json,
      }});
  }
}

export function* getReviewSaga() {
  yield takeLatest(GET_REVIEW, getReview);
}
