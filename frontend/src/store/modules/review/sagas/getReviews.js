import { put, takeLatest } from 'redux-saga/effects';

import * as http from '../../../../utils/http';
import { GET_REVIEWS, SET_REVIEWS } from '../actions';

function* getReviews(action) {
  const params = action.payload;
  
  const result = yield http.get('/api/reviews/', params);
  
  if (result.status === 200) {
    yield put({ type: SET_REVIEWS, payload: {
        list: result.json.results,
      }})
  }
}

export function* getReviewsSaga() {
  yield takeLatest(GET_REVIEWS, getReviews)
}
