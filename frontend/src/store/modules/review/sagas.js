import { all } from 'redux-saga/effects';

import { getReviewSaga } from './sagas/getReview';
import { getReviewsSaga } from './sagas/getReviews';

export default function* combinedSagas() {
  yield all([
    getReviewSaga(),
    getReviewsSaga(),
  ]);
}
